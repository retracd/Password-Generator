#A simple password generator
#Programmed fully by Brent Mayes. Original Creation.

import string
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font

HEIGHT = 275
WIDTH = 575
root = tk.Tk()
root.title("PasswordGenerator")

#defines the password generator function, it really is super simple
def pwgen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):
    password = ''.join(random.choice(chars) for _ in range(size))
    passoutput.insert(INSERT, (password))

#defines a function hooked up to a button that clears the output
def clearoutput():
    passoutput.delete('1.0', 'end')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='#d630e6')
canvas.pack()

maintitle = tk.Label(root, text="Password Generator", font=('Jokerman', 18), fg='#35393d', bg='#30e661', anchor='n')
maintitle.place(relx=0.28, rely=0.04, relwidth=0.44, relheight=0.12)

mainframe = tk.Frame(root, bg='#94b2e3')
mainframe.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)

numlabel = tk.Label(mainframe, text="Number of Characters Long", font=('Chiller', 18), fg='#5882c7', bg='#94b2e3')
numlabel.place(relx=0.2, rely=0.02, relwidth=0.6, relheight=0.1)

numinput = tk.Entry(mainframe, font=('Wingdings', 12), justify='left')
numinput.place(relx=0.1, rely=0.14, relwidth=0.8, relheight=0.16)

genbutton = tk.Button(mainframe, text="Generate", font=('Jokerman', 10), bg='#e8f229', activebackground='#3b5887', command=lambda: pwgen(int(numinput.get())))
genbutton.place(relx=0.2, rely=0.34, relwidth=0.2, relheight=0.1)

clearbutton = tk.Button(mainframe, text="Clear", font=('Jokerman', 10), bg='#e8f229', activebackground='#3b5887', command=lambda: clearoutput())
clearbutton.place(relx=0.6, rely=0.34, relwidth=0.2, relheight=0.1)

passlabel = tk.Label(mainframe, text="Your Password", font=('Chiller', 18), fg='#5882c7', bg='#94b2e3')
passlabel.place(relx=0.3, rely=0.48, relwidth=0.4, relheight=0.1)

passoutput = tk.Text(mainframe, font=('Vivaldi', 12), bg='#e04612')
passoutput.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.3)


root.mainloop()
