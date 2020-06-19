from scripts.frenchword import FrenchWord

def main():

    my_word = input("French To English Tanslator V1\n\nInput \"00QUIT00\" to Quit\nEnter Sentence Here : ")
    my_word_list = my_word.split()

    if my_word == "00QUIT00": quit()

    for x in range(len(my_word_list)):

        my_french_word = FrenchWord(my_word_list[x])

        try: my_french_word.getenglishtranslation()
        except: print("[error] Sorry, an Error Occured")
    
    main()

if __name__ == "__main__": 
    main()