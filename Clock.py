from tkinter import *
from time import strftime
import datetime


root = Tk()
root.title("Clock")

def time():
    x = datetime.datetime.now()
    str = x.strftime('%X')
    str1 = x.strftime('%x')
    lbl.config(text=str)
    lbl.after(1000, time)
    lbl1.config(text=str1)

lbl = Label(root, bg="blue", fg="white", font="calibri 40 bold")
lbl.pack(anchor=CENTER)

lbl1 = Label(root, bg="black", fg="white", font='Calibri 20 bold')
lbl1.pack()
x = datetime.datetime.now()
time()
root.mainloop()