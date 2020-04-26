class Film:
    """
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
    """
    def __init__(self, title, year, url, rate, poster_url):
        self.title = title
        self.year = year
        self.url = url
        self.rate = rate
        self.poster_url = poster_url

    def __str__(self):
        return str(self.title) + " (" + str(self.year) + ") " + str(self.rate) + " " + str(self.url)

    def getTitleWithYear(self):
        return str(self.title) + " (" + str(self.year) + ")"
