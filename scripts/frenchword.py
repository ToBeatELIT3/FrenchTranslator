from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as BeautifulSoup
import sys

sys.stoud = open("test.txt", "a+")

class FrenchWord:

    def __init__(self, word):
        self.word = word

    def test(self):
        pass