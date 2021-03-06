class File:
    """
    A class used to input/output operation
    and contain information from file.

    Attributes
    ----------
    file_name : str
        a name of file to read/write list of films to skip
        default value is "films_to_skip.txt"
    filmsToSkip : list
        a list of films, that are viewed by user
        and should be skipped

    Methods
    -------
    getFilmsToSkip()
        returns filmsToSkip list
    addFilmsToSkip(newFilm)
        add Film object given as newFilm to list filmsToSkip
    save()
        save filmsToSkip list to file
    """
    def __init__(self, file_name="films_to_skip.txt"):
        self._file_name = file_name
        try:
            f = open(self._file_name, "r")
            self.filmsToSkip = f.read().splitlines()
            f.close()
        except FileNotFoundError:
            self.filmsToSkip = []

    def getFilmsToSkip(self):
        return self.filmsToSkip

    def addFilmsToSkip(self, new_film):
        if type(new_film) == str:
            self.filmsToSkip.append(new_film)

    def save(self):
        f = open(self._file_name, "w")
        f.seek(0)
        for film in self.filmsToSkip:
            f.write(film + "\n")
        f.truncate()
        f.close()
