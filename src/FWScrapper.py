from requests import get
from bs4 import BeautifulSoup
from Film import Film
from random import randrange
from urllib3 import exceptions as urllib3
from requests import exceptions as requests


class FWScrapper:
    """
    A class responsible for download required date from Filmweb website
    and choose a random film.

    Attributes
    ----------
    categories : dict
        dictionary makes string into number,
        needed to construct correct url address
    listOfFilms : list
        a list of film that are downloaded last time
    currentCategory : str
        a name of category that was searched last time

    Methods
    -------
    getRandomFilm(chosen_category, minimal_rate, file)
        returns random film from chosen category
        if category is incorrect returns None
    downloadDescription(film)
        returns short description from Filmweb website
        for the film given as parameter
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
        page = get(url)
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
        if minimal_rate > '8':
            minimal_rate = '8'
        if chosen_category not in FWScrapper.categories:
            return None

        if FWScrapper.currentCategory != chosen_category or not FWScrapper.listOfFilms:
            FWScrapper.listOfFilms = []
            try:
                FWScrapper.listOfFilms = FWScrapper._downloadListOfFilms(chosen_category)
                FWScrapper.currentCategory = chosen_category
            except (urllib3.NewConnectionError, urllib3.MaxRetryError, requests.ConnectionError):
                return None

        final_list = [f for f in FWScrapper.listOfFilms if f.rate >= minimal_rate and f.getTitleWithYear() not in file.getFilmsToSkip()]
        i = 2
        while len(final_list) < 5 and i < 10:
            try:
                FWScrapper.listOfFilms = FWScrapper.listOfFilms + FWScrapper._downloadListOfFilms(chosen_category, i)
            except (urllib3.NewConnectionError, urllib3.MaxRetryError, requests.ConnectionError):
                return None
            i = i + 1
            final_list = [f for f in FWScrapper.listOfFilms if f.rate >= minimal_rate and f.getTitleWithYear() not in file.getFilmsToSkip()]

        if not final_list:
            return None
        else:
            random_choice = randrange(0, len(final_list))
            return final_list[random_choice]

    @staticmethod
    def downloadDescription(film):
        if type(film) == Film:
            try:
                page = get(film.url)
            except (urllib3.NewConnectionError, urllib3.MaxRetryError, requests.ConnectionError):
                return None
            soup = BeautifulSoup(page.content, 'html.parser')
            description = soup.find(class_='filmPosterSection__plot').text
            return description
        else:
            return None
