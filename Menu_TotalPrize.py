# # from multiprocessing.sharedctypes import Value
# # from struct import pack
# # import tkinter as tk
# # from tkinter import *

# # root=tk.Tk()
# # root.title('Window')
# # root.geometry("500x300")

# # var = tk.StringVar()

# # def print_selection():
# #     l.config(text='Total Prize : ' +var.get())



# # Checkbutton1 = tk.Checkbutton(root,text='Pizza 200',onvalue=1, offvalue=0, variable=var,command=print_selection)
# # Checkbutton1.pack()

# # Checkbutton2 = tk.Checkbutton(root,text='Burger 60',onvalue=1, offvalue=0,variable=var,command=print_selection)
# # Checkbutton2.pack()

# # Checkbutton3 = tk.Checkbutton(root,text='Sandwich 25',onvalue=1, offvalue=0,variable=var,command=print_selection)
# # Checkbutton3.pack()

# # Checkbutton4 = tk.Checkbutton(root,text='Sandwich 25',onvalue=1, offvalue=0,variable=var,command=print_selection)
# # Checkbutton4.pack()

# # l = tk.Label(root,bg='white',width=15,text='')
# # l.pack()


# # root.mainloop()

# import tkinter as tk
 

# window = tk.Tk()
# window.title('My Window')
# window.geometry('600x600')
 

 
# def print_selection():
#     if (var1.get() == 1) & (var2.get() == 0):
#         l.config(text='Pizza 200 ')
#     elif (var1.get() == 0) & (var2.get() == 1):
#         l.config(text='Burger 150')
#     elif (var1.get() == 0) & (var3.get() == 1):
#         l.config(text='Sandwich 25')
#     elif (var1.get() == 0) & (var4.get() == 1):
#         l.config(text='Maggi 25')
#     elif (var1.get() == 0) & (var2.get() == 0):
#         (var1.get() == 0) & (var3.get() == 0)
#         (var1.get() == 0) & (var4.get() == 0)
#         l.config(text='Select Menu')
#     else:
#         l.config(text=':)')
 
# var1 = tk.IntVar()
# var2 = tk.IntVar()
# var3 = tk.IntVar()
# var4 = tk.IntVar()
# c1 = tk.Checkbutton(window, text='Pizza 200',variable=var1, onvalue=1, offvalue=0, command=print_selection)
# c1.pack()
# c2 = tk.Checkbutton(window, text='Burger 150',variable=var2, onvalue=1, offvalue=0, command=print_selection)
# c2.pack()
# c3 = tk.Checkbutton(window, text='Sandwich 25',variable=var3, onvalue=1, offvalue=0, command=print_selection)
# c3.pack()
# c4 = tk.Checkbutton(window, text='Maggi 25',variable=var4, onvalue=1, offvalue=0, command=print_selection)
# c4.pack()
# l = tk.Label(window, bg='white', width=25, text='empty')
# l.pack()
 
# window.mainloop()

import tkinter
 
window_main = tkinter.Tk(className='Tkinter - TutorialKart', )
window_main.geometry("450x250")
 
check_1 = tkinter.IntVar()
check_2 = tkinter.IntVar()
check_3 = tkinter.IntVar()
 
def check1Clicked():
    if check_1.get() :
        print('Checkbox 1 selected')
    else :
        print('Checkbox 1 unselected')
 
def check2Clicked():
    if check_2.get() :
        print('Checkbox 2 selected')
    else :
        print('Checkbox 2 unselected')
 
def check3Clicked():
    if check_3.get() :
        print('Checkbox 3 selected')
    else :
        print('Checkbox 3 unselected')
 
check_but_1 = tkinter.Checkbutton(window_main, text = 'Listening to Music', variable = check_1,
                onvalue = 1, offvalue = 0, command=check1Clicked)
check_but_1.pack()
 
check_but_2 = tkinter.Checkbutton(window_main, text = 'Reading Books', variable = check_2,
                onvalue = 1, offvalue = 0, command=check2Clicked)
check_but_2.pack()
 
check_but_3 = tkinter.Checkbutton(window_main, text = 'Watching Movies', variable = check_3,
                onvalue = 1, offvalue = 0, command=check3Clicked)
check_but_3.pack()
 
window_main.mainloop()