## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Documentation](#documentation)

## General info
Project developed for Scripting Languages class (AGH UST).\

A task of application is to draw a film from Filmweb website.\
A user can specify details, such as category and minimal rate.\
Films marked as viewed by user are skipped during the drawing.

![Main Window](screenshots/main_window.png)

## Technologies
Project is created with:
* Python 3.6.9
* Tkinter 8.6\
graphical user interface library
* BeautifulSoup 4.9\
library for pulling data out of HTML and XML files

## Setup
To run this project:
```
$ python3 main.py
```

## Documentation
All classes and methods are documented. Check e.g.
```
>>> print(Film.__doc__)

    A class used to represent a film.

    Attributes
    ----------
    title : str
        the title of the film
    year : str
        the release date of the film
    url : str
        url address to information about film on Filmweb website
    rate : int
        the rate of the film on Filmweb website
    poster_url : str
        url address of the film poster

    Methods
    -------
    getTitleWithYear()
        returns str contains title and release date of the film
        e.g. "Iron Man (2008)"
```
