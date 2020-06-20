#ToBeatElite
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import validators

def getpagesouphtml(url):

    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    
    page_soup = soup(page_html, "html.parser")

    return page_soup

def testurlvalid(url, word):

        if validators.url(url):
            try: 
                getpagesouphtml(url).findAll("div")
                return True

            except: 
                print(f"[error] {word} is an Invalid Word")
                return False

        else: 
            print(f"[error] {word} is an Invalid Word")
            return False
