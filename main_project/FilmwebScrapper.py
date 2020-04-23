import requests
from bs4 import BeautifulSoup
from Film import Film
from random import randrange


class FilmwebScrapper:
    categories = {
        "Akcja": 28,
        "Animacja": 2,
        "Dokumentalny": 5,
        "Familijny": 8
    }

    listOfFilms = []
    currentCategory = ""

    @staticmethod
    def downloadListOfFilms(chosen_category):
        results = []
        for i in range(1, 3):
            try:
                url = "https://www.filmweb.pl/films/search?genres=" + str(FilmwebScrapper.categories["Akcja"]) + "&orderBy=popularity&descending=true&page=" + str(i)
                page = requests.get(url)
                soup = BeautifulSoup(page.content, 'html.parser')
                results = results + soup.find_all(class_='FilmPreview filmPreview filmPreview--FILM Film')

                for elem in results:
                    title = elem.find(class_='filmPreview__title')
                    FilmwebScrapper.listOfFilms.append(Film(title.text, "url"))
                FilmwebScrapper.currentCategory = chosen_category
            except:
                break

    @staticmethod
    def getRandomFilm(chosen_category):
        if FilmwebScrapper.currentCategory != chosen_category or not FilmwebScrapper.listOfFilms:
            FilmwebScrapper.downloadListOfFilms(chosen_category)

        random_choice = randrange(0, len(FilmwebScrapper.listOfFilms))
        return FilmwebScrapper.listOfFilms[random_choice]


if __name__ == "__main__":
    print(FilmwebScrapper.getRandomFilm("Animacja"))
