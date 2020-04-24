class Film:
    def __init__(self, title, year, url, rate):
        self.title = title
        self.year = year
        self.url = url
        self.rate = rate

    def __str__(self):
        return str(self.title) + " (" + str(self.year) + ") " + str(self.rate) + " " + str(self.url)

    def getTitleWithYear(self):
        return str(self.title) + " (" + str(self.year) + ")"
