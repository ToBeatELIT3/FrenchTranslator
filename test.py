from scripts.englishword import EnglishWord
from urllib.request import urlopen as uReq
from scripts.frenchword import FrenchWord
from bs4 import BeautifulSoup as soup

#myword = EnglishWord("testeyesutf")
frword = FrenchWord("bon")
frword.getdefinition()
"""
def scrape2():
    uClient = uReq("https://www.le-dictionnaire.com/definition/pain")
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    my_list = []

    definition = page_soup.find("div", class_="defbox").li.select("a")

    for x in range(len(definition)):
        my_list.append(definition[x].text.strip())

    print(" ".join(my_list))
"""
