#ToBeatElite
from .utils import getpagesouphtml, testurlvalid
import unidecode

class FrenchWord:

    def __init__(self, word):

        try:

            self.word = unidecode.unidecode(word.replace(" ", "").lower())

            self.fr_url = f"https://www.le-dictionnaire.com/definition/{self.word}"

            self.page_soup_frtoen_url = getpagesouphtml(f"https://dictionary.cambridge.org/dictionary/french-english/{self.word}")
            self.page_soup_fr_url = getpagesouphtml(f"https://www.le-dictionnaire.com/definition/{self.word}")
            self.page_soup_fr_exaples_url = getpagesouphtml( f"https://www.kikiladi.com/citation.php?mot={self.word}")
            self.isvalid = True

        except:
            self.word = "invalid_word"
            self.isvalid = False 

    def getpagehtml(self):
        if not self.isvalid or not testurlvalid(self.fr_url, self.word): 
            return None

        with open(f"downloaded_html/{self.word}_frtoen_webpage.html", "w", encoding="utf-8") as filename: 
            filename.write(f"{self.page_soup_frtoen_url}")

        with open(f"downloaded_html/{self.word}_fr_webpage.html", "w", encoding="utf-8") as filename:
            filename.write(f"{self.page_soup_fr_url}")

    def getdefinition(self):
        if not self.isvalid or not testurlvalid(self.fr_url, self.word): return None
        my_list = []

        definition = self.page_soup_fr_url.find("div", class_="defbox").li.select("a")

        for x in range(len(definition)):
            my_list.append(unidecode.unidecode(definition[x].text.strip()))

        my_definition = " ".join(my_list)

        print(f"The Definition of {self.word} is: {my_definition}")
        return my_definition

    def getexamples(self):
        if not self.isvalid or not testurlvalid(self.fr_url, self.word): return None

        wordexamples = self.page_soup_fr_exaples_url.find("ul", class_="citation").select("li")

        wordexamples_returnlist = []

        for x in range(len(wordexamples)):
            print(f"Example {x}: {unidecode.unidecode(wordexamples[x].text.strip())}\n")
            wordexamples_returnlist.append(unidecode.unidecode(wordexamples[x].text.strip()))
        
        return wordexamples_returnlist

    def getenglishtranslation(self):
        if not self.isvalid or not testurlvalid(self.fr_url, self.word): return None

        englishword = self.page_soup_frtoen_url.find("span", class_="trans dtrans")
        englishword = englishword.text.strip().split(" ", 1)[0]

        print(f"{self.word} en English est: {englishword}")
        return englishword
