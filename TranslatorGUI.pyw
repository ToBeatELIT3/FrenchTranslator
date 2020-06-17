from scripts.englishword import EnglishWord
from scripts.frenchword import FrenchWord
from tkinter import *

root = Tk()
root.title("Translator V1")
root.geometry("500x290")
root.resizable(False, False)
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file="resources/file.png"))

def start():
    pass

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
start_button = Button(root, text="Translate", command=start, width=20, height=5)
english_language_randiobutton = Radiobutton(root, text="English To French", variable=language_option_intvar, value=1)
french_language_radiobutton = Radiobutton(root, text="French To English", variable=language_option_intvar, value=2)
give_examples_checkbutton = Checkbutton(root, text="Give Examples", variable=give_examples_intvar)
download_html_checkbutton = Checkbutton(root, text="Download HTML", variable=download_html_intvar)
easy_translate_checkbutton = Checkbutton(root, text="Easy Translate", variable=easy_translate_intvar)

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

if __name__ == "__main__" : root.mainloop()