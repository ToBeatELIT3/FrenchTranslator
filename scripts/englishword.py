from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from .frenchword import FrenchWord
import sys

class EnglishWord(FrenchWord):

    def __init__(self, word):
        self.word = word.replace(" ", "")
        self.my_url = (f"https://www.wordreference.com/enfr/{self.word}")

        uClient = uReq(self.my_url)
        page_html = uClient.read()
        uClient.close()

        self.page_soup = soup(page_html, "html.parser")

    def getpagehtml(self):
        sys.stdout = open(f"{self.word}_webpage.html", "a+")
        print(self.page_soup)

    def getfrenchtranslaton(self):
        frenchword = self.page_soup.find("", class_="")
        frenchword = FrenchWord(frenchword.text.strip) 
        return frenchword.word
