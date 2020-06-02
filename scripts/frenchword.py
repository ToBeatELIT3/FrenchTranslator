from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

class FrenchWord:

    def __init__(self, word):
        self.word = word.replace(" ", "").lower()
        self.frtoen_url = (f"https://www.linguee.com/french-english/search?source=auto&query={self.word}")
        self.fr_url = (f"https://www.dictionary.com/browse/{self.word}?s=ts")

        uClient = uReq(self.frtoen_url)
        page_html = uClient.read()
        uClient.close()

        self.page_soup_frtoen_url = soup(page_html, "html.parser")

        uClient = uReq(self.fr_url)
        page_html = uClient.read()
        uClient.close()

        self.page_soup_fr_url = soup(page_html, "html.parser")

    def getpagehtml(self):

        with open(f"html/{self.word}_frtoen_webpage.html", "w", encoding="utf-8") as filename: 
            filename.write(f"{self.page_soup_frtoen_url}")

        with open(f"html/{self.word}_fr_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_fr_url}")

    def getdefinition(self):
        pass
        #worddefinition =self.page_soup_fr_url.find("", class_="")
        #worddefinition = worddefinition.text.strip()

        #print(f"The Definition of {self.word} is: {worddefinition}")
        #return worddefinition
