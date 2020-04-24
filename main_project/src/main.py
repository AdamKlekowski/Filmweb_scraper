"""
Adam Klekowski
"""

from File import *
from GUI import GUI

if __name__ == "__main__":
    f = File("films_to_skip.txt")
    g = GUI(f)
    g.run()
    f.save()
