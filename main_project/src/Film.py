class Film:
    """
    A class used to represent a film.

    Attributes
    ----------
    title : str
    year : str
        the name of the animal
    url : str
        the sound that the animal makes
    rate : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
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
