from tkinter.ttk import Combobox
from tkinter import *
from FWScrapper import FWScrapper


class GUI:
    def __init__(self, file):
        self._file = file

        self.window = Tk()
        self.window.title("Losuj film!")
        self.window.geometry('660x540')

        self.listbox = Combobox(self.window)
        self.listbox['values'] = [item for item in FWScrapper.categories]
        self.listbox.current(0)
        self.listbox.grid(column=1, row=1)
        self.rate = Spinbox(self.window, from_=1, to=9)
        self.rate.grid(column=1, row=2)

        self.runButton = Button(self.window, text='Losuj film!', command=self.drawFilm)
        self.runButton.grid(column=2, row=2)

        self.skipButton = Button(self.window, text='Już widziałem!', command=self.markAsViewed)
        self.skipButton.grid(column=3, row=2)

        self.foundFilm = Label(self.window, text='')
        self.foundFilm.grid(column=1, row=4)

    def drawFilm(self):
        film = FWScrapper.getRandomFilm(self.listbox.get(), self.rate.get(), self._file)
        if not film:
            self.foundFilm.config(text="Film not found")
        else:
            self.foundFilm.config(text=film.getTitleWithYear())

    def markAsViewed(self):
        if self.foundFilm["text"] and self.foundFilm["text"] != "Film not found":
            self._file.addFilmsToSkip(self.foundFilm["text"])
        self.drawFilm()

    def run(self):
        self.window.mainloop()
