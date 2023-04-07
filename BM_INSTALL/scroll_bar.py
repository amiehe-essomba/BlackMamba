from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox 

def scroll_bar(frame, char):    
    scrollbar_v = Scrollbar(frame, orient=VERTICAL)
    scrollbar_v.pack(side=RIGHT, fill=BOTH, ipady=5)
    
    scrollbar_h =  Scrollbar(frame, orient=HORIZONTAL)
    scrollbar_h.pack(fill=BOTH, side=BOTTOM, ipadx=5)
    
    my_list = Listbox(frame, yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)

    my_list.insert(END, "   ")
    my_list.pack(fill=BOTH, expand=YES)
    
    scrollbar_v.config(command=my_list.yview)
    scrollbar_h.config(command=my_list.xview)
    
    return my_list
    