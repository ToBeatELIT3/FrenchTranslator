from scripts.englishword import EnglishWord
from scripts.frenchword import FrenchWord

def translate(word):
    enword = EnglishWord(word)

    return enword.getfrenchtranslaton()

def main(word):
    wordlist = word.split()
    
    for x in range(len(wordlist)):
        translate(wordlist[x])

if __name__ == "__main__":
    main(input("Paragraph: "))
    