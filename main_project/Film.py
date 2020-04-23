class Film:
    title = ""
    url = ""

    def __init__(self, title, url):
        self.title = title
        self.url = url

    def __str__(self):
        return str(self.title)
