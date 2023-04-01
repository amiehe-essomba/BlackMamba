from tkinter import *
from PIL import Image, ImageTk

def commands_desactivation(frame1, frame2, root):     
    frame1.destroy()
    frame2.destroy()
    
    frame1 = LabelFrame(root, relief=FLAT, bd = 5, width=390, height=350, 
                            text='BLACK MAMBA PROGRAMM INSTALLATION', font=("calibri", 10, 'bold'), bg="white")
    frame2 =  Frame(root, relief=FLAT, bd = 5, width=390, height=45, bg="white")
    frame1.place(x=0, y=0, width=390, height=350) 
    frame2.place(x=0, y=360, width=390, height=45)
    
    List = ['Select location']
    height = 40
    frame_1 =  Frame(frame1,  bd = 5, width=390, height=height, relief=GROOVE, bg="white")
    frame_2 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    frame_3 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    frame_4 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    
    frame_1.place(x=0, y=150, width=300, height=height )
    frame_2.place(x=0, y=190, width=300, height=height )
    frame_3.place(x=0, y=230, width=300, height=height )
    frame_4.place(x=0, y=280, width=250, height=height )
    
    label1 = Button(frame_1, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
            width=50, height=50,  relief=GROOVE, anchor='w', state=DISABLED)
    label1.pack()
    
    install_btn = Button(frame2, text='install', state=DISABLED, width=10, relief=GROOVE)
    install_btn.place(x=0, y=0)
    install_btn.destroy()
    
    prev_btn = Button(frame2, text='previous', state=DISABLED, width=10, relief=GROOVE)
    prev_btn.place(x=280, y=4)