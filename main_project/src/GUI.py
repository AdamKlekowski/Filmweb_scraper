import os
import urllib
from tkinter.ttk import Combobox
from tkinter import *
from FWScrapper import FWScrapper
from PIL import Image, ImageTk
from tkinter.font import Font

class GUI:
    def __init__(self, file):
        self._file = file

        self.window = Tk()
        self.window.title("Losuj film!")
        self.window.minsize(660, 420)
        self.window.maxsize(660, 420)

        # font style ---------------------------------------------
        widgetStyle = Font(family="Lucida Grande", size=12)
        titleStyle = Font(family="Lucida Grande", size=14)

        # tkinter widget -----------------------------------------
        self.categoryLabel = Label(self.window, text='Gatunek:', font=widgetStyle)
        self.categoryLabel.grid(column=1, row=1)
        self.listbox = Combobox(self.window, font=widgetStyle)
        self.listbox['values'] = [item for item in FWScrapper.categories]
        self.listbox.current(0)
        self.listbox.grid(column=2, row=1)

        self.rateLabel = Label(self.window, text='Minimalna ocena:', font=widgetStyle)
        self.rateLabel.grid(column=1, row=2)
        self.rate = Spinbox(self.window, from_=1, to=8, font=widgetStyle)
        self.rate.grid(column=2, row=2)

        self.info = Label(self.window, text='Film wylosownay dla Ciebie:')
        self.info.grid(column=1, row=4)

        self.foundFilm = Label(self.window, text='', font=titleStyle)
        self.foundFilm.place(x=220, y=90)

        self.runButton = Button(self.window, text='Losuj film!', command=self.drawFilm)
        self.runButton.place(x=220, y=360)

        self.skipButton = Button(self.window, text='Już widziałem!', command=self.markAsViewed)
        self.skipButton.place(x=350, y=360)

    def loadImg(self, film):
        if film:
            url = film.poster_url
            urllib.request.urlretrieve(url, 'poster.jpg')

            load = Image.open("poster.jpg")
            render = ImageTk.PhotoImage(load)
            self.imgLabel = Label(self.window, image=render)
            self.imgLabel.img = render
            self.imgLabel.grid(column=1, row=5)

            os.remove("poster.jpg")
        else:
            self.imgLabel.config(image=None) #TODO to fix

    def drawFilm(self):
        film = FWScrapper.getRandomFilm(self.listbox.get(), self.rate.get(), self._file)
        if not film:
            self.foundFilm.config(text="Film not found")
        else:
            self.foundFilm.config(text=film.getTitleWithYear())
        self.loadImg(film)

    def markAsViewed(self):
        if self.foundFilm["text"] and self.foundFilm["text"] != "Film not found":
            self._file.addFilmsToSkip(self.foundFilm["text"])
        self.drawFilm()

    def run(self):
        self.window.mainloop()
