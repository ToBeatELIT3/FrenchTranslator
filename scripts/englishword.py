#ToBeatElite
from .utils import getpagesouphtml, testurlvalid
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

class EnglishWord:

    def __init__(self, word):

        try:
            self.word = word.replace(" ", "").lower()

            self.en_url = f"https://www.dictionary.com/browse/{self.word}?s=ts"

            self.page_soup_entofr_url = getpagesouphtml(f"https://www.linguee.com/english-french/search?source=auto&query={self.word}")
            self.page_soup_en_url = getpagesouphtml(f"https://www.dictionary.com/browse/{self.word}?s=ts")

        except: 
            self.word = "invalid_word"
            print("Invalid Word")

    def getpagehtml(self):
        if not testurlvalid(self.en_url, self.word): return None

        with open(f"downloaded_html/{self.word}_entofr_webpage.html", "w", encoding="utf-8") as filename: 
            filename.write(f"{self.page_soup_entofr_url}")

        with open(f"downloaded_html/{self.word}_en_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_en_url}")

    def getdefinition(self):
        if not testurlvalid(self.en_url, self.word): return None
        
        worddefinition = self.page_soup_en_url.find("span", class_="one-click-content css-1p89gle e1q3nk1v4")
        worddefinition = worddefinition.text.strip()

        print(f"The Definition of {self.word} is: {worddefinition}")
        return worddefinition
    
    def getexaples(self):
        if not testurlvalid(self.en_url, self.word): return None

        wordexaples = self.page_soup_en_url.findAll("p", class_="one-click-content css-a8m74p e15kc6du6")
    
        wordexaples_returnlist = []

        for x in range(len(wordexaples)):
            print(f"Example {x}: {wordexaples[x].text.strip()}\n")
            wordexaples_returnlist.append(wordexaples[x].text.strip())
        
        return wordexaples_returnlist

    def getfrenchtranslaton(self):
        if not testurlvalid(self.en_url, self.word): return None

        if self.word == "i":
            print(f"{self.word} in French is: je")
            return "je"

        elif self.word == "a":
            print(f"{self.word} in French is: a")
            return "a"

        frenchword = self.page_soup_entofr_url.find("a", class_="dictLink featured")
        frenchword = frenchword.text.strip().split(" ", 1)[0]

        print(f"{self.word} in French is: {frenchword}")
        return frenchword
