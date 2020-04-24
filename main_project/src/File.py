class File:

    def __init__(self, file_name):
        self._file_name = file_name
        f = open(self._file_name, "r")
        self.filmsToSkip = f.read().splitlines()
        f.close()

    def getFilmsToSkip(self):
        return self.filmsToSkip

    def addFilmsToSkip(self, newFilm):
        self.filmsToSkip.append(newFilm)

    def save(self):
        f = open(self._file_name, "w")
        f.seek(0)
        for film in self.filmsToSkip:
            f.write(film + "\n")
        f.truncate()
        f.close()
