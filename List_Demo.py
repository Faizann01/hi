import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("300x200")
listSample = Listbox(root,width=70,height=10,fg='blue',font=("Arial 28"))
listSample.insert(1,"Dominos")
listSample.insert(2,"Lapinos")
listSample.insert(3,"Pizza Hut")

listSample.pack()
root.mainloop()

