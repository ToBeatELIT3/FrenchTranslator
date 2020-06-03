from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import os

class FrenchWord:

    def __init__(self, word):

        try:
            self.word = word.replace(" ", "").lower()
            self.frtoen_url = (f"https://www.linguee.com/english-french/search?source=french&query={self.word}")
        #  self.en_url = (f"https://www.dictionary.com/browse/{self.word}?s=ts")