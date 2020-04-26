import os
from urllib import request
from tkinter.ttk import Combobox
from tkinter import *
from FWScrapper import FWScrapper
from PIL import Image, ImageTk
from tkinter.font import Font
from Film import Film


class GUI:
    """
    A class responsible for Graphical User Interface.

    Methods
    -------
    _loadImg()
        downloads and loads into proper label a film poster
        if film is not found, clears proper label
    _drawFilm()
        calls FWScrapper.getRandomFilm() in order to get Film object
        load information about film to proper labels
        if FWScrapper.getRandomFilm() returns None, clears proper labels
    _markAsViewed()
        passes the current film to File.addFilmsToSkip()
    run()
        run tkinter mainloop()
    """
    def __init__(self, file):
        self._file = file

        self.window = Tk()
        self.window.title("Losuj film!")
        self.window.minsize(660, 400)
        self.window.maxsize(660, 400)

        # font style ---------------------------------------------
        self.widgetStyle = Font(family="Lucida Grande", size=12)
        self.titleStyle = Font(family="Lucida Grande", size=14)

        # tkinter widgets -----------------------------------------
        self.categoryLabel = Label(self.window, text='Gatunek:', font=self.widgetStyle)
        self.categoryLabel.place(x=5, y=5)
        self.listbox = Combobox(self.window, font=self.widgetStyle)
        self.listbox['values'] = [item for item in FWScrapper.categories]
        self.listbox.current(0)
        self.listbox.place(x=180, y=5)

        self.rateLabel = Label(self.window, text='Minimalna ocena:', font=self.widgetStyle)
        self.rateLabel.place(x=5, y=30)
        self.rate = Spinbox(self.window, from_=1, to=8, font=self.widgetStyle)
        self.rate.place(x=180, y=30)

        # tkinter widgets contain info about film -----------------
        self.imgLabel = Label(self.window)
        self.imgLabel.place(x=5, y=60)

        self.info = Label(self.window, text='Film wylosowany dla Ciebie:')
        self.info.place(x=220, y=60)

        self.titleLabel = Label(self.window, text='Wciśnij Losuj!', font=self.titleStyle)
        self.titleLabel.place(x=220, y=90)

        try:
            load = Image.open("img/star.png")
            load = load.resize((40, 40))
            render = ImageTk.PhotoImage(load)
            self.starLabel = Label(self.window, image=render)
            self.starLabel.img = render
            self.starLabel.place(x=220, y=130)
        except FileNotFoundError:
            pass

        self.rateLabel = Label(self.window, text='-', font=self.titleStyle)
        self.rateLabel.place(x=270, y=140)

        self.descriptionLabel = Message(self.window, text='', width=350)
        self.descriptionLabel.place(x=220, y=190)

        # tkinter buttons -----------------------------------------
        self.runButton = Button(self.window, text='Losuj film!', command=self._drawFilm)
        self.runButton.place(x=300, y=350)

        self.skipButton = Button(self.window, text='Już widziałem!', command=self._markAsViewed)
        self.skipButton.place(x=420, y=350)

    def _loadImg(self, film):
        if film and type(film) == Film:
            url = film.poster_url
            request.urlretrieve(url, 'poster.jpg')

            load = Image.open("poster.jpg")
            render = ImageTk.PhotoImage(load)
            self.imgLabel.config(image=render)
            self.imgLabel.img = render

            os.remove("poster.jpg")
        else:
            self.imgLabel.img = None

    def _drawFilm(self):
        film = FWScrapper.getRandomFilm(self.listbox.get(), self.rate.get(), self._file)
        if not film:
            self.titleLabel.config(text="Nie znaleziono filmu.")
            self.rateLabel.config(text="-")
            self.descriptionLabel.config(text="")
        else:
            self.titleLabel.config(text=film.getTitleWithYear())
            self.rateLabel.config(text=film.rate + "/10")
            self.descriptionLabel.config(text=FWScrapper.downloadDescription(film))
        self._loadImg(film)

    def _markAsViewed(self):
        if self.titleLabel["text"] and self.titleLabel["text"] != "Nie znaleziono filmu.":
            self._file.addFilmsToSkip(self.titleLabel["text"])
        self._drawFilm()

    def run(self):
        self.window.mainloop()
