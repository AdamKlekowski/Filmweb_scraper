#Adam Klekowski

from tkinter.ttk import Combobox
from tkinter import *
from FWScrapper import FWScrapper

if __name__ == "__main__":
    window = Tk()
    window.title("Losuj film!")
    window.geometry('660x540')

    listbox = Combobox(window)
    listbox['values'] = [item for item in FWScrapper.categories]
    listbox.current(0)
    listbox.grid(column=1, row=1)

    rate = Spinbox(window, from_=1, to=9)
    rate.grid(column=1, row=2)

    def clicked():
        film = FWScrapper.getRandomFilm(listbox.get())
        foundFilm.config(text=film.title + " " + film.rate)

    runButton = Button(window, text='Losuj film!', command=clicked)
    runButton.grid(column=2, row=2)

    foundFilm = Label(window, text='')
    foundFilm.grid(column=1, row=4)

    window.mainloop()

