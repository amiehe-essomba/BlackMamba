import os, sys 
import time 
from io import StringIO
import alive_progress as AP
from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import  Combobox, Progressbar
#from BM_INSTALL import left_frame
from BM_INSTALL import right_frame
import BM_TAR

def ico_path():
    system  = os.uname()[0]
    if system == 'Linux':
        return "@"+os.path.abspath(os.curdir)+'/images/logo.xbm'
    else:  return None 

def png_path(str_ : str = 'logo.png'):
    system  = "Linux"
    if system == 'Linux':
        return os.path.abspath(os.curdir)+f'/images/{str_}'
    else:  return None 
    
def read_license():
    path = os.path.abspath(os.curdir)+"/BM_TAR/LICENSE"
    with open(path, 'r') as f:
        lines = f.readlines()
    f.close()
    return lines

def extraction_tar_gz():
    ico_path_ = "@"+ico_path()
    
    a, b, c = 600, 400, 200
    root = Tk()
    root.title("Black Mamba 1.01.01 64-bit")
    root.geometry(f"{a}x{b}")
    root.minsize(a, b)
    root.maxsize(a, b)
    root.config(bg='white')
    root_menu = Menu(root)
    #root.iconbitmap("@logo.xbm")
    root.resizable(width=True, height=True)
    
    frame_left = Frame(root, relief=RIDGE, bd = 4, width=c, height=b)
    frame_left.place(x=0, y=0)
    
    #left_frame.configure(root=frame_left, figure=png_path('galaxy.png' ))
    
    frame_right = Frame(root, relief=RAISED, bd = 4, width=a-c, height=b)
    frame_right.place(x=c, y=0)
     
    sub_frame_right2 =  right_frame.scrollbar_right(frame_right=frame_right, main_root=root, ico_path=ico_path(), license=read_license())
    right_frame.right(ico_path=ico_path(), main_root=root).cancel(root=sub_frame_right2)
    
    root.mainloop() 

if __name__ == '__main__':
    extraction_tar_gz()