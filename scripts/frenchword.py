from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as BeautifulSoup
import sys

class FrenchWord:

    def __init__(self, word):
        self.word = word.replace(" ", "").lower()
        self.frtoen_url = (f"https://www.linguee.com/french-english/search?source=auto&query={self.word}")
        self.fr_url = (f"https://www.dictionary.com/browse/{self.word}?s=ts")
