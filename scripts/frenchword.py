from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import sys

class FrenchWord:

    def __init__(self, word):

        try: 
            self.word = word.replace(" ", "").lower()
            self.frtoen_url = f"https://www.linguee.com/french-english/search?source=french&query={self.word}"
            self.fr_url = f"https://www.le-dictionnaire.com/definition/{self.word}"
            self.fr_exaples = f"https://www.kikiladi.com/citation.php?mot={self.word}"
            uClient = uReq(self.frtoen_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_frtoen_url = soup(page_html, "html.parser")

            uClient = uReq(self.fr_url)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_fr_url = soup(page_html, "html.parser")

            uClient = uReq(self.fr_exaples)
            page_html = uClient.read()
            uClient.close()

            self.page_soup_fr_exaples_url = soup(page_html, "html.parser")
            self.isvalid = True

        except: self.isvalid = False 

    def getpagehtml(self):
        if not testwordvalid(self.fr_url, self.word, self.page_soup_fr_url) or not self.isvalid: return None

        with open(f"html/{self.word}_frtoen_webpage.html", "w", encoding="utf-8") as filename: 
            filename.write(f"{self.page_soup_frtoen_url}")

        with open(f"html/{self.word}_fr_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_fr_url}")

    def getdefinition(self):
        if not testwordvalid(self.fr_url, self.word, self.page_soup_fr_url) or not self.isvalid: return None
        my_list = []

        definition = self.page_soup_fr_url.find("div", class_="defbox").li.select("a")

        for x in range(len(definition)):
            my_list.append(definition[x].text.strip())

        my_definition = " ".join(my_list)

        print(f"The Definition of {self.word} is: {my_definition}")
        return my_definition

    def getexamples(self):
        if not testwordvalid(self.fr_url, self.word, self.page_soup_fr_url) or not self.isvalid: return None

        wordexamples = self.page_soup_fr_exaples_url.find("ul", class_="citation").select("li")

        for x in range(len(wordexamples)):
            print(f"Example {x}: {wordexamples[x].text.strip()}\n")      

def testwordvalid(my_url, word, page_soup):
        try: 
            definition = page_soup.find("div", class_="defbox").li.select("a")
            return True
        except:
             
            print(f"[error] {word} is an Invalid Word")
            return False
