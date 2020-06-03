from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys
import os

class FrenchWord:

    def __init__(self, word):

        try: 
            self.word = word.replace(" ", "").lower()
            self.frtoen_url = f"https://www.linguee.com/french-english/search?source=french&query={self.word}"
            self.fr_url = f"https://www.le-dictionnaire.com/definition/{self.word}"

            uClient = uReq(self.frtoen_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_frtoen_url = soup(page_html, "html.parser")

            uClient = uReq(self.fr_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_fr_url = soup(page_html, "html.parer")

        except: print("Invalid Word")

    def getpagehtml(self):
        if not testwordvalid(self.fr_url, self.word):
            os.remove(f"html/{self.word}_fr_webpage.html")
            os.remove(f"html/{self.word}_frtoen_webpage.html")
            return None

        with open(f"html/{self.word}_frtoen_webpage.html", "w", encoding="utf-8") as filename: 
            filename.write(f"{self.page_soup_frtoen_url}")

        with open(f"html/{self.word}_fr_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_fr_url}")

    def getexamples(self):
        if not testwordvalid(self.fr_url, self.word): return None
        
        worddefinition = self.page_soup_fr_url.findAll("div", class_="defbox")
        worddefinition = worddefinition.text.strip()

        for words in range(len(worddefinition)):
            myword = worddefinition[words].a
            print(myword)
            
def testwordvalid(url, word):
        try: 
            uClient = uReq(url)
            return True
        except: 
            print(f"[error] {word} is an Invalid Word")
            return False
