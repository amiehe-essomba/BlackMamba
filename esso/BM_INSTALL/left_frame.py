from tkinter import *
from PIL import Image

def configure(root, figure):
    frame = Frame(root, relief=FLAT, width=190, height=390, bg ='ivory')
    frame.place(x=0, y=0)
     
    path = figure 
    img  = Image.open( path ) 
    
    img = img.resize((190, 390), Image.ANTIALIAS ) 
    img  = ImageTk.PhotoImage( img ) 
    panel = Label(frame, image=img) 
    panel.image  = img 
    panel.pack() 