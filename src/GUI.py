import os
import urllib
from tkinter.ttk import Combobox
from tkinter import *
from FWScrapper import FWScrapper
from PIL import Image, ImageTk
from tkinter.font import Font


class GUI:
    """
    A class used to

    Methods
    -------
    run()
        run tkinter mainloop
    """
    def __init__(self, file):
        self._file = file

        self.window = Tk()
        self.window.title("Losuj film!")
        self.window.minsize(660, 400)
        self.window.maxsize(660, 400)

        # font style ---------------------------------------------
        widgetStyle = Font(family="Lucida Grande", size=12)
        titleStyle = Font(family="Lucida Grande", size=14)

        # tkinter widget -----------------------------------------
        self.categoryLabel = Label(self.window, text='Gatunek:', font=widgetStyle)
        self.categoryLabel.place(x=5, y=5)
        self.listbox = Combobox(self.window, font=widgetStyle)
        self.listbox['values'] = [item for item in FWScrapper.categories]
        self.listbox.current(0)
        self.listbox.place(x=180, y=5)

        self.rateLabel = Label(self.window, text='Minimalna ocena:', font=widgetStyle)
        self.rateLabel.place(x=5, y=30)
        self.rate = Spinbox(self.window, from_=1, to=8, font=widgetStyle)
        self.rate.place(x=180, y=30)

        self.info = Label(self.window, text='Film wylosowany dla Ciebie:')
        self.info.place(x=220, y=60)

        self.titleLabel = Label(self.window, text='Wciśnij Losuj!', font=titleStyle)
        self.titleLabel.place(x=220, y=90)

        load = Image.open("img/star.png")
        load = load.resize((40, 40))
        render = ImageTk.PhotoImage(load)
        self.starLabel = Label(self.window, image=render)
        self.starLabel.img = render
        self.starLabel.place(x=220, y=130)

        self.rateLabel = Label(self.window, text='-', font=titleStyle)
        self.rateLabel.place(x=270, y=140)

        self.descriptionLabel = Message(self.window, text='', width=350)
        self.descriptionLabel.place(x=220, y=190)

        self.runButton = Button(self.window, text='Losuj film!', command=self.drawFilm)
        self.runButton.place(x=300, y=350)

        self.skipButton = Button(self.window, text='Już widziałem!', command=self.markAsViewed)
        self.skipButton.place(x=420, y=350)

    def loadImg(self, film):
        if film:
            url = film.poster_url
            urllib.request.urlretrieve(url, 'poster.jpg')

            load = Image.open("poster.jpg")
            render = ImageTk.PhotoImage(load)
            self.imgLabel = Label(self.window, image=render)
            self.imgLabel.img = render
            self.imgLabel.place(x=5, y=60)

            os.remove("poster.jpg")
        else:
            self.imgLabel = Label(self.window, image=None)
            self.imgLabel.img = None

    def drawFilm(self):
        film = FWScrapper.getRandomFilm(self.listbox.get(), self.rate.get(), self._file)
        if not film:
            self.titleLabel.config(text="Nie znaleziono filmu.")
            self.rateLabel.config(text="-")
            self.descriptionLabel.config(text="")
        else:
            self.titleLabel.config(text=film.getTitleWithYear())
            self.rateLabel.config(text=film.rate)
            self.descriptionLabel.config(text=FWScrapper.downloadDescription(film))
        self.loadImg(film)

    def markAsViewed(self):
        if self.titleLabel["text"] and self.titleLabel["text"] != "Nie znaleziono filmu.":
            self._file.addFilmsToSkip(self.titleLabel["text"])
        self.drawFilm()

    def run(self):
        self.window.mainloop()
