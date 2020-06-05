from scripts.englishword import EnglishWord
from urllib.request import urlopen as uReq
from scripts.frenchword import FrenchWord
from bs4 import BeautifulSoup as soup

#myword = EnglishWord("testeyesutf")
frword = FrenchWord("elle")
frword.getexamples()
