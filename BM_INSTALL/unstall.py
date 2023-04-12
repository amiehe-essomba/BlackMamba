from tkinter import *
from tkinter import messagebox , filedialog
from BM_INSTALL import right_frame
import os 
import shutil

def unstall_new_window(frame1, frame2, root, main_root, ico_path, license): 
    global check_bnt_int
    root_path = os.path.abspath(os.curdir)
    
    List    = ['Select location']
    height  = 40
    FRAME   =  Frame(main_root,  bd = 5, width=400, height=350, relief=RAISED, bg="white")
    FRAME.place(x=200, y=0)
    FRAME0  =  Frame(main_root,  bd = 5, width=400, height=50, relief=RAISED, bg="white")
    FRAME0.place(x=200, y=360)
    
    frame0  =  LabelFrame(FRAME, bd=5, width=390, height=height, relief=FLAT, text="BLACK MAMBA UNINSTALLATION PROGRAMM",
                        font = ('calibri', 10, 'bold'), bg="white")
    frame1 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame2 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame3 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame4 = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    frame0.place(x=0, y=0, height=150)
    frame1.place(x=0, y=150, height=height, width=300)
    frame2.place(x=0, y=190, height=height, width=300)
    frame3.place(x=0, y=230, height=height, width=300)
    frame4.place(x=0, y=270, height=height, width=300)
    
    label1 = Button(frame1, text=List[0], state=NORMAL, font=('calibi', 10, 'bold', 'underline'),
                        foreground="blue", width=50, height=50, relief=GROOVE, anchor='w',
                        command=lambda : PATH(frame2, frame3, label1, FRAME))
    label1.pack()
    
    install_btn = Button(FRAME0, text="install", state=DISABLED, width=9,  relief=GROOVE )
    install_btn.place(x=0, y=4)
    
    prev_btn = Button(FRAME0, text="previous", state=NORMAL, width=9,  relief=GROOVE,
                    command=lambda : right_frame.nex_section(FRAME, FRAME0, root, main_root, ico_path, license ))
    prev_btn.place(x=100, y=4)
    
    return prev_btn, frame1, frame2


def PATH(frame, frame_, btn,  FRAME ):
    height = 5
    frame.destroy()
    frame = Frame(FRAME, bd=5, width=400, height=height, relief=FLAT, bg='white' )
    __path__root = filedialog.askdirectory()  
    
    if __path__root:
        try:
            Path1 = __path__root  + "/BlackMamba"
            if "BlackMamba" in os.listdir(__path__root):
                if os.path.isdir(Path1) is True:
                    shutil.rmtree(Path1)
                    message(frame_, "Successfully uninstall !")
                    btn.config(state=DISABLED)
                else: message(frame )
            else: message(frame )
        except Exception : message(frame )
    else: pass 
    

def message(frame, m = 'Black Mamba is not already installed !'  ):
    entree = Entry(frame,  font=('arial', 10, 'bold'), foreground='blue', width=50 ) 
    entree.pack()
    entree.insert(0, '')
    entree.delete(0, END)
    entree.insert(0, f"{m}")
    entree.config(state=DISABLED, bg='ivory')