from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox , filedialog
from BM_INSTALL import right_frame
from BM_INSTALL import unzip_and_compress as unzip
import os 

def unstall_new_window(frame1, frame2, root, main_root, ico_path): 
    global check_bnt_int
    
    frame1.destroy()
    frame2.destroy()
    frame1 = LabelFrame(root, relief=FLAT, bd = 5, width=390, height=350, 
                            text='BLACK MAMBA UNINSTALLATION PROGRAMM', font=("calibri", 10, 'bold'), bg="white")
    frame2 =  Frame(root, relief=FLAT, bd = 5, width=390, height=45, bg="white")
    frame1.place(x=0, y=0, width=390, height=350) 
    frame2.place(x=0, y=360, width=390, height=45)
    
    List = ['Select location']
    height = 40
    frame_1 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    frame_2 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    frame_3 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    frame_4 =  Frame(frame1,  bd = 5, width=390, height=height, relief=FLAT, bg="white")
    
    frame_1.place(x=0, y=150, width=300, height=height )
    frame_2.place(x=0, y=190, width=300, height=height )
    frame_3.place(x=0, y=230, width=300, height=height )
    frame_4.place(x=0, y=280, width=250, height=height )
        
    install_btn = Button(frame2, text='uninstall', state=DISABLED, width=10, relief=GROOVE)
    install_btn.place(x=0, y=0)
    
    prev_btn = Button(frame2, text='previous', state=NORMAL, width=10, relief=GROOVE, 
                    command=lambda : right_frame.nex_section(frame1, frame2, root, main_root, ico_path ))
    prev_btn.place(x=85, y=0)
    
    return prev_btn, frame1, frame_1
    
