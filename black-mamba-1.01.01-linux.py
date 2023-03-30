import os, sys 
import time 
from io import StringIO
import alive_progress as AP

try: 
    from Tkinter import Tk
    from tkinter import messagebox 
    from tkinter.ttk import  Combobox, Progressbar
except ImportError:
    from tkinter import Tk
    from tkinter import messagebox 
    from tkinter.ttk import  Combobox, Progressbar

def ico_path():
    system  = os.uname()[0]
    if system == 'Linux':
        return os.path.abspath(os.curdir)+'/images/logo.ico'
    else:  return None 

def get_path():
    return None

def save_path():
    return None 

def extraction_tar_gz():
    root = Tk()
    root.title("Black Mamba Installation")
    root.geometry("400x200")
    root.minsize("400x200")
    root.maxsize("400x200")
    root.config('white')
    root_menu = Menu(root)
    root.iconbitmap(ico_path())
    
    root.mainloop()
    #return None 

if __name__ == '__main__':
    extraction_tar_gz()