import os, sys 
import time 
from io import StringIO
import alive_progress as AP
from tkinter import *
from tkinter import messagebox 
from tkinter.ttk import  Combobox, Progressbar
from PIL import Image, ImageTk

def ico_path():
    system  = "Linux"
    if system == 'Linux':
        return os.path.abspath(os.curdir)+'/images/logo.ico'
    else:  return None 

def png_path(str_ : str = 'logo.png'):
    system  = "Linux"
    if system == 'Linux':
        return os.path.abspath(os.curdir)+f'\images\{str_}'
    else:  return None 

def destroy_root( root ):    
    messagebox.showinfo("Welcome to GFG.",  "Hi I'm your message")
    root.destroy()

def get_path():
    return None

def save_path():
    return None 

def extraction_tar_gz():
    root = Tk()
    root.title("Black Mamba Installation")
    root.geometry("600x400")
    root.minsize(600, 400)
    root.maxsize(600, 400)
    root.config(bg='white')
    root_menu = Menu(root)
    root.iconbitmap(ico_path())
    root.resizable(width=True, height=True)
    
    frame_left = Frame(root, relief=RIDGE, bd = 4, width=200, height=400)
    frame_left.place(x=0, y=0)
    
    f1_left = Frame(frame_left, relief=FLAT, width=190, height=200)
    f1_left.place(x=0, y=0)
    
    f2_left = Frame(frame_left, relief=FLAT, width=190, height=190, bg ='ivory')
    f2_left.place(x=0, y=210)
    
    path_, path__ = png_path( ), png_path('galaxy.png' )
    img1, img2 = Image.open( path_ ), Image.open( path__ )
    
    img1, img2 = img1.resize((170, 170), Image.ANTIALIAS ), img2.resize((190, 180), Image.ANTIALIAS )
    img1, img2 = ImageTk.PhotoImage( img1 ), ImageTk.PhotoImage( img2 )
    panel1, panel2 = Label(f1_left, image=img1), Label(f2_left, image=img2)
    panel1.image, panel2.image = img1, img2 
    panel1.pack(), panel2.pack()
    label1 = Label(f1_left, text="Black Mamba", font=("Arial", 18, 'bold'))
    label1.pack() 
    
    frame_right = Frame(root, relief=FLAT, bd = 4, width=400, height=400)
    frame_right.place(x=200, y=0)
    
    cancel = Button(frame_right, width=5, text='cancel', command =  lambda : destroy_root(root), state=NORMAL)
    cancel.place(x=300, y=350)
    
    root.mainloop() 

if __name__ == '__main__':
    extraction_tar_gz()