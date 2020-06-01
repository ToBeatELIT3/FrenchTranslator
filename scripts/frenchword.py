from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys


class FrenchWord:

    def __init__(self, word):
        self.word = word
        self.my_url = (f"https://www.linguee.com/english-french/search?source=auto&query={self.word}")

        uClient = uReq(self.my_url)
        page_html = uClient.read()
        uClient.close()

        self.page_soup = soup(page_html, "html.parser")
    
    def test(self):
        pass

    def getworddefinition(self):
        worddefinition = self.page_soup.find("", class_="")

        return worddefinition.text.strip()

