#ToBeatElite
from scripts.englishword import EnglishWord
from scripts.frenchword import FrenchWord
from tkinter import *
import threading

root = Tk()
root.title("Translator V1")
root.geometry("500x290")
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="resources/file.png"))

def easytranslate():
    if easy_translate_intvar.get() == 1:
        give_examples_checkbutton.config(state=DISABLED)
        download_html_checkbutton.config(state=DISABLED)

    if easy_translate_intvar.get() == 0:
        give_examples_checkbutton.config(state=NORMAL)
        download_html_checkbutton.config(state=NORMAL)

def starttranslation():
    startthread = threading.Thread(target=translate)
    startthread.start()

def translate():
    try:
        start_button.config(state=DISABLED)

        if sentance_stringvar.get() == "Example Text" or file_name_stringvar.get() == "Example File Name": 
            start_button.config(state=NORMAL)
            return None

        my_word_list = sentance_stringvar.get().split()

        for x in range(len(my_word_list)):

            if language_option_intvar.get() == 1:
                my_english_word = EnglishWord(my_word_list[x])

                if my_english_word.word != "invalid_word":

                    my_english_word_translation = my_english_word.getfrenchtranslaton()
                    
                    my_english_word_defintion = my_english_word.getdefinition()

                    if give_examples_intvar.get() == 1:
                        my_english_word_examples = my_english_word.getexaples() 

                    if download_html_intvar.get() == 1 and easy_translate_intvar.get() != 1:
                        my_english_word.getpagehtml()

                    if easy_translate_intvar.get() == 1:
                        with open(f"output_files/{file_name_stringvar.get()}_easytranslate.txt", "a+", encoding="UTF-8") as filename:
                            filename.write(f"{my_english_word_translation} ")

                    elif easy_translate_intvar.get() == 0:
                        
                        with open(f"output_files/{file_name_stringvar.get()}.txt", "a+", encoding="UTF-8") as filename:
                            filename.write(f"{my_english_word.word} in French is : {my_english_word_translation}\n")
                            filename.write(f"The Definition of {my_english_word.word} is : {my_english_word_defintion}\n")
                        
                            try:
                                for x in range(len(my_english_word_examples)):
                                    filename.write(f"Example {x} : {my_english_word_examples[x]}\n")
                        
                            except: pass
           
                else: 
                    with open(f"output_files/{file_name_stringvar.get()}.txt", "w+") as filename:
                        filename.write(f"[ERROR] THERE IS AN INVALID WORD\nQUITTING")

            elif language_option_intvar.get() == 2:
                my_french_word = FrenchWord(my_word_list[x])

                if my_french_word.word != "invalid_word":

                    my_french_word_translation = my_french_word.getenglishtranslation()

                    my_french_word_definition = my_french_word.getdefinition()

                    if give_examples_intvar.get() == 1:
                        my_french_word_examples = my_french_word.getexamples()

                    if download_html_intvar.get() ==1:
                        my_french_word.getpagehtml()

                    if easy_translate_intvar.get() == 1:
                        with open(f"output_files/{file_name_stringvar.get()}_easytranslate.txt", "a+") as filename:
                            filename.write(f"{my_french_word_translation} ")

                    elif easy_translate_intvar.get() == 0:
                        with open(f"output_files/{file_name_stringvar.get()}.txt", "a+", encoding="UTF-8") as filename:
                            filename.write(f"{my_french_word.word} in English is : {my_french_word_translation}\n")
                            filename.write(f"The Definition of {my_french_word.word} is : {my_french_word_definition}\n")

                            try:
                                for x in range(len(my_french_word_examples)):
                                    filename.write(f"Example {x} : {my_french_word_examples[x]}\n")
                            
                            except: pass
            
                else:
                    if easy_translate_intvar.get() == 0:
                        with open(f"outpur_files/{file_name_stringvar.get()}.txt", "w+") as filename:
                            filename.write(f"[ERROR] THERE IS AN INVALID WORD\nQUITTING")

                    elif easy_translate_intvar.get() == 1:
                        with open(f"outpur_files/{file_name_stringvar.get()}_easytranslate.txt", "w+") as filename:
                            filename.write(f"[ERROR] THERE IS AN INVALID WORD\nQUITTING")

        start_button.config(state=NORMAL)

    except: 
        start_button.config(state=NORMAL)
        return None

    start_button.config(state=NORMAL)

sentance_stringvar = StringVar()
file_name_stringvar = StringVar()

language_option_intvar = IntVar()
give_examples_intvar = IntVar()
download_html_intvar = IntVar()
easy_translate_intvar = IntVar()

sentance_stringvar.set("Example Text")
file_name_stringvar.set("Example File Name")

language_option_intvar.set("1")
easy_translate_intvar.set("1")

title_label = Label(root, text="English & French Translator V1", font=("Courier", 20))
sentance_entry_label = Label(root, text="Enter Sentance Here: ")
sentance_entry = Entry(root, textvariable=sentance_stringvar, width=55)
filename_entry_label = Label(root, text="Enter Desired File Name : ")
filename_entry = Entry(root, textvariable=file_name_stringvar, width=55)
start_button = Button(root, text="Translate", command=starttranslation, width=20, height=5)
english_language_randiobutton = Radiobutton(root, text="English To French", variable=language_option_intvar, value=1)
french_language_radiobutton = Radiobutton(root, text="French To English", variable=language_option_intvar, value=2)
give_examples_checkbutton = Checkbutton(root, text="Give Examples", variable=give_examples_intvar)
download_html_checkbutton = Checkbutton(root, text="Download HTML", variable=download_html_intvar)
easy_translate_checkbutton = Checkbutton(root, text="Easy Translate", variable=easy_translate_intvar, command=easytranslate)

title_label.grid(row=1, column=1, columnspan=100, sticky=W)
sentance_entry_label.grid(row=2, column=1, sticky=W, padx=10)
sentance_entry.grid(row=2, column=2, sticky=W)
filename_entry_label.grid(row=3, column=1, sticky=W, padx=10)
filename_entry.grid(row=3, column=2, sticky=W)
start_button.grid(row=4, column=1, sticky=W, padx=5)
english_language_randiobutton.grid(row=5, column=1, sticky=W, padx=10)
french_language_radiobutton.grid(row=6, column=1, sticky=W, padx=10)
give_examples_checkbutton.grid(row=7, column=1, sticky=W, padx=10)
download_html_checkbutton.grid(row=8, column=1, sticky=W, padx=10)
easy_translate_checkbutton.grid(row=9, column=1, sticky=W, padx=10)

if __name__ == "__main__" : 
    easytranslate()    
    root.mainloop()
