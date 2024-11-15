from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator #pip install googletrans==3.1.0a0
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

frame1= Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#C5C6C7')
frame1.place(x=0, y=0)

Label(root, text="Language Translator", font=("Helvetica 20 bold"), fg="black", bg='#C5C6C7').pack(pady=10)


def translate():
    lang_1 = text_entry1.get("1.0", "end")
    cl = choose_language.get()

    if not lang_1.strip():
        messagebox.showerror('Language Translator','Enter the text to translate!')
    else:
            text_entry2.delete(1.0, 'end')
            translator = Translator()
            output = translator.translate(lang_1, dest=cl)
            text_entry2.insert('end', output.text)

def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a = tk.StringVar()

auto_select = ttk.Combobox(frame1, width=27, textvariable= a, state='randomly', font=('verdana', 10, 'bold'))

auto_select['values'] = (
                            'Auto Select',
                        )

auto_select.place(x=15, y=60)
auto_select.current(0)                       

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='randomly', font=('verdana', 10, 'bold'))

choose_language['values'] = (
                            'Afrikaans',
                            'Albanian',
                            'Arabic',
                            'Armenian',
                            'Azerbaijani',
                            'Basque',
                            'Belarusian',
                            'Bengali',
                            'Bosnian',
                            'Bulgarian',
                            'Catalan',
                            'Cebuano',
                            'chichewa',
                            'Chinese',
                            'Corsican',
                            'Croatian',
                            'Czech',
                            'Danish',
                            'Dutch',
                            'English',
                            'Esperanto',
                            'Estonian',
                            'Filipino',
                            'Finnish',
                            'French',
                            'Frisian',
                            'Galician',
                            'Georgian',
                            'German',
                            'Greek',
                            'Gujarati',
                            'Haitian Creole',
                            'Hausa',
                            'Hawalian',
                            'Hebrew',
                            'Hindi',
                            'Haong',
                            'Hungarian',
                            'Icelandic',
                            'Igbo',
                            'Indonesian',
                            'Irish',
                            'Italian',
                            'Japanese',
                            'Javanese',
                            'Kannada',
                            'Kazakh',
                            'Kinyarwanda',
                            'Korean',
                            'Kurdish',
                            'Kyrgyz',
                            'Lao',
                            'Latin',
                            'Latvian',
                            'Lithuanian',
                            'Macedonian',
                            'Malagasy',
                            'Malay',
                            'Malayalam',
                            'Maltese',
                            'Maori',
                            'Marathi',
                            'Mongolian',
                            'Myanmar',
                            'Nepali',
                            'Norwegian',
                            'Odia',
                            'Pashto',
                            'Persian',
                            'Polish',
                            'Portuguese',
                            'Punjabi',
                            'Romanian',
                            'Russian',
                            'Samoan',
                            'Scots Gaelic',
                            'Serbian',
                            'Sesotho',
                            'Shona',
                            'Sindhi',
                            'Sinhala',
                            'Slovak',
                            'Slovenian',
                            'Somali',
                            'spanish',
                            'Sondanese',
                            'Swahili',
                            'Swedish',
                            'Tajik',
                            'Tamil',
                            'Tatar',
                            'Telugu',
                            'Thai',
                            'Turkish',
                            'Turkmen',
                            'Ukrainian',
                            'Urdu',
                            'Uyghur',
                            'Uzbek',
                            'Vietnamese',
                            'Welsh',
                            'Xhosa',
                            'Yiddish',
                            'Yoruba',
                            'Zulu'
                            )


choose_language.place(x=305, y=60)
choose_language.current(0)

text_entry1 =Text(frame1,width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=100)

text_entry2 = Text(frame1,width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=100)

btn1 = Button(frame1, command=translate, text= "Translate", relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg="white",cursor="hand2")
btn1.place(x=185, y=300)

btn2= Button(frame1, command=clear, text="Clear",relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2', fg="white",cursor="hand2" )
btn2.place(x=300, y=300)

root.mainloop()