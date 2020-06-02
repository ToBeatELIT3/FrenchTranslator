from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import os

class EnglishWord:

    def __init__(self, word):

        try:
            self.word = word.replace(" ", "").lower()
            self.entofr_url = (f"https://www.linguee.com/english-french/search?source=auto&query={self.word}")
            self.en_url = (f"https://www.dictionary.com/browse/{self.word}?s=ts")

            uClient = uReq(self.entofr_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_entofr_url = soup(page_html, "html.parser")

            uClient = uReq(self.en_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_en_url = soup(page_html, "html.parser")

        except: print("Invalid Word")

    def getpagehtml(self):
        try:
            with open(f"html/{self.word}_entofr_webpage.html", "w", encoding="utf-8") as filename: 
                filename.write(f"{self.page_soup_entofr_url}")

            with open(f"html/{self.word}_en_webpage.html", "w", encoding="utf-8") as filename:
                filename.write(f"{self.page_soup_en_url}")
        
        except: 
            print(f"[error] {self.word}is an Invalid Word")
            os.remove(f"html/{self.word}_en_webpage.html")
            os.remove(f"html/{self.word}_entofr_webpage.html")

    def getdefinition(self):
        try:
            worddefinition =self.page_soup_en_url.find("span", class_="one-click-content css-1p89gle e1q3nk1v4")
            worddefinition = worddefinition.text.strip()

            print(f"The Definition of {self.word} is: {worddefinition}")
            return worddefinition
        
        except: print(f"[error] {self.word} is an Invalid Word")
    
    def getexaples(self):
        try:
            wordexaples = self.page_soup_en_url.findAll("p", class_="one-click-content css-a8m74p e15kc6du6")
        
            for x in range(len(wordexaples)):
                print(f"Example {x}: {wordexaples[x].text.strip()}\n")

        except: print(f"[error] {self.word}  is an Invalid Word")

    def getfrenchtranslaton(self):
        try:
            frenchword = self.page_soup_entofr_url.find("a", class_="dictLink featured")
            frenchword = frenchword.text.strip().split(" ", 1)[0]

            print(f"{self.word} in French is: {frenchword}")
            return frenchword

        except: print(f"[error] {self.word} is an Invalid Word")
