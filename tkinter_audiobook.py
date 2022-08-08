from cProfile import label
from tkinter import *
from tkinter.filedialog import *
import pyttsx3
import PyPDF2

parent = Tk()
parent.title("PyAudioBook")
parent.geometry("400x400")
engine = pyttsx3.init()
v = DoubleVar()  
var = IntVar()

def test():
    rate = engine.getProperty('rate')
    engine.setProperty('rate',v.get())
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[var.get()].id)
    engine.say("The quick brown fox jumps over the lazy dog")
    engine.runAndWait()

def talk():
    rate = engine.getProperty('rate')
    engine.setProperty('rate',v.get())
    engine.say(text_entry.get())
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[var.get()].id)
    engine.runAndWait()

def browse():
    book = askopenfilename()
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    for x in range(0,pages):
        page = pdfreader.getPage(x)
        text = page.extractText()
        rate = engine.getProperty('rate')
        engine.setProperty('rate',v.get())
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[var.get()].id)
        engine.say(text)
        engine.runAndWait

def clear():
    text_entry.delete(0,END)

setting_labelframe = LabelFrame(parent, text="Settings", width = 380, height = 180)  
setting_labelframe.place(x=10, y = 10)

gender_label = Label(setting_labelframe, text= "Select voice:")
gender_label.place(x= 20, y= 20 )

male_RadButton = Radiobutton(setting_labelframe, text = "male", variable= var, value = 0)
male_RadButton.place(x= 100,y=20)

female_RadButton = Radiobutton(setting_labelframe, text = "female", variable= var, value = 1)
female_RadButton.place(x= 100,y=40)

Rate_label = Label(setting_labelframe, text="Select speech rate(160 recommended):")
Rate_label.place(x= 20, y = 80)

rateScale = Scale(setting_labelframe,variable = v, from_ = 50, to = 500, orient = HORIZONTAL)  
rateScale.place(x = 240, y=60)

test_button = Button(setting_labelframe, text = 'Test and Apply',command=test)
test_button.place(x= 20, y = 120)

audiobook_labelframe = LabelFrame(parent, text = "Audiobook", height = 180, width = 380)
audiobook_labelframe.place(x = 10, y= 200)

browse_label = Label(audiobook_labelframe, text = "Browse pdf to listen:")
browse_label.place(x = 20, y  = 20)

browse_button = Button(audiobook_labelframe, text='browse',command=browse)
browse_button.place(x=140,y=15)

or_label = Label(audiobook_labelframe, text = "OR")
or_label.place(x = 80, y = 40)

text_label = Label(audiobook_labelframe, text= "Enter custom text:")
text_label.place(x=20, y = 60)

text_entry = Entry(audiobook_labelframe)
text_entry.place(x=125,y=60) 

clear_button = Button(audiobook_labelframe, text = "clear", command=clear)
clear_button.place(x=260, y = 55)

speak_button = Button(audiobook_labelframe, text='Speak',command=talk)
speak_button.place(x=150,y=120)

parent.mainloop()