from scripts.englishword import EnglishWord

def main():

    my_word = input("Enter Sentence Here : ")
    my_word_list = my_word.split()

    if my_word == "00QUIT00": quit()

    for x in range(len(my_word_list)):

        my_english_word = EnglishWord(my_word_list[x])

        try: my_english_word.getfrenchtranslaton()
        except: print("[error] Sorry, an Error Occured")
    
    main()

if __name__ == "__main__": 
    print("English To French Translator V1\n\nInput \"00QUIT00\" to Quit\n")
    main()