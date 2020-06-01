from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
#from .frenchword import FrenchWord
import sys

class EnglishWord:

    def __init__(self, word):
        self.word = word.replace(" ", "").lower()
        self.entofr_url = (f"https://www.linguee.com/english-french/search?source=auto&query={self.word}")
        self.en_url = (f"https://www.dictionary.com/browse/{self.word}?s=ts")

    def getpagehtml(self):

        with open(f"html/{self.word}_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_entofr}")

    def getdefinition(self):
        uClient = uReq(self.en_url)
        page_html = uClient.read()
        uClient.close()

        page_soup_en_url = soup(page_html, "html.parser")

        worddefinition = page_soup_en_url.find("span", class_="one-click-content css-1p89gle e1q3nk1v4")
        worddefinition = worddefinition.text.strip()

        print(f"The Definition of {self.word} is: {worddefinition}")
        return worddefinition
    
    def getexaples(self):
        uClient = uReq(self.en_url)
        page_html = uClient.read()
        uClient.close()

        page_soup_en_url = soup(page_html, "html.parser")

        wordexaples = page_soup_en_url.findAll("p", class_="one-click-content css-a8m74p e15kc6du6")
        
        for x in range(len(wordexaples)):
            print(f"Example {x}: {wordexaples[x].text.strip()}\n")

    def getfrenchtranslaton(self):
        uClient = uReq(self.entofr_url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html, "html.parser")

        frenchword = page_soup.find("a", class_="dictLink featured")
        frenchword = frenchword.text.strip().split(" ", 1)[0]

        print(f"{self.word} in French is: {frenchword}")
        return frenchword
