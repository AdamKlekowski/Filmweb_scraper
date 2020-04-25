import requests
from bs4 import BeautifulSoup
from Film import Film
from random import randrange


class FWScrapper:
    """
    A class responsible for download required date form Filmweb website
    and choose a random film.

    Attributes
    ----------
    categories : dict
        ...

    Methods
    -------
    _downloadListOfFilms(chosen_category, num_page=1)
        ...
    getRandomFilm(chosen_category, minimal_rate, file)
        ...
    """
    categories = {
        "Akcja": 28,
        "Animacja": 2,
        "Dokumentalny": 5,
        "Dramat": 6,
        "Familijny": 8,
        "Fantasy": 9,
        "Horror": 12,
        "Komedia": 13,
        "Krótkometrażowy": 50,
        "Kryminał": 15,
        "Melodramat": 16,
        "Niemy": 67,
        "Przygodowy": 20,
        "Romans": 32,
        "Sci-Fi": 33
    }

    listOfFilms = []
    currentCategory = ""

    @staticmethod
    def _downloadListOfFilms(chosen_category, num_page=1):
        results = []

        url = "https://www.filmweb.pl/films/search?genres=" + str(
            FWScrapper.categories[chosen_category]) + "&orderBy=popularity&descending=true&page=" + str(num_page)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        hits_item_lists = soup.find_all(class_='hits__item')

        for elem in hits_item_lists:
            title = elem.find(class_='filmPreview__title').text
            year = elem.find(class_='filmPreview__year').text
            rate = elem.find(class_='rateBox__rate').text
            link = "https://www.filmweb.pl" + elem.find(class_='filmPreview__link')["href"]
            img_src = elem.find('img')["data-src"]

            results.append(Film(title, year, link, rate, img_src))
        return results

    @staticmethod
    def getRandomFilm(chosen_category, minimal_rate, file):
        if FWScrapper.currentCategory != chosen_category or not FWScrapper.listOfFilms:
            FWScrapper.listOfFilms = []
            try:
                FWScrapper.listOfFilms = FWScrapper._downloadListOfFilms(chosen_category)
                FWScrapper.currentCategory = chosen_category
            except:
                return None

        finalListOfFilm = [film for film in FWScrapper.listOfFilms if film.rate >= minimal_rate and film.getTitleWithYear() not in file.getFilmsToSkip()]
        i = 2
        while len(finalListOfFilm) == 0 and i < 5:
            try:
                FWScrapper.listOfFilms = FWScrapper.listOfFilms + FWScrapper._downloadListOfFilms(chosen_category, i)
            except:
                return None
            i = i + 1
            finalListOfFilm = [film for film in FWScrapper.listOfFilms if film.rate >= minimal_rate and film.getTitleWithYear() not in file.getFilmsToSkip()]

        if not finalListOfFilm:
            return None
        else:
            random_choice = randrange(0, len(finalListOfFilm))
            return finalListOfFilm[random_choice]

    @staticmethod
    def downloadDescription(film):
        if type(film) == Film:
            try:
                page = requests.get(film.url)
            except:
                return None
            soup = BeautifulSoup(page.content, 'html.parser')
            description = soup.find(class_='filmPosterSection__plot').text
            return description
        else:
            return None
