from cProfile import label
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("clock")
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)

lbl = Label(root, font = ('Times new roman',40,'bold') , background = 'purple' , foreground ='white')

lbl.pack(anchor ='center')
time()

mainloop()