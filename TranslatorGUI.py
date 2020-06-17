from scripts.englishword import EnglishWord
from scripts.frenchword import FrenchWord
from tkinter import *

root = Tk()
root.title("Translator V1")
#root.geometry()
#root.resizable(False, False)
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

title_label = Label(root, text="English & French Translator V1", width=200, font=("Courier", 20))
sentance_entry_label = Label(root, text="Enter Sentance Here: ")
sentance_entry = Entry(root, textvariable=sentance_stringvar)
filename_entry_label = Label(root, text="Enter Desired File Name : ")
filename_entry = Entry(root, textvariable=file_name_stringvar)
start_button = Button(root, text="Translate", command=start)
english_language_randiobutton = Radiobutton(root, text="English To French", variable=language_option_intvar, value=1)
french_language_radiobutton = Radiobutton(root, text="French To English", variable=language_option_intvar, value=2)
give_examples_checkbutton = Checkbutton(root, text="Give Examples", variable=give_examples_intvar, value=1)
download_html_checkbutton = Checkbutton(root, text="Download HTML", variable=download_html_intvar, value=1)
easy_translate_checkbutton = Checkbutton(root, text="Easy Translate", variable=easy_translate_intvar, value=1)

if __name__ == "__main__" : root.mainloop()