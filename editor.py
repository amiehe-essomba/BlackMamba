from tkinter import *
from script.STDIN.LinuxSTDIN import bm_configure as bm

def run():
    string = bm.words(ide.get('1.0', END), bm.fg.rbg(255,255,255)).final()
    print(string)

win = Tk()
win.title("esso")
m = Menu(win)
r = Menu(m, tearoff=0)
r.add_command(label='run', command=run)
m.add_cascade(label='run', menu=r )
win.config(menu=m)
ide = Text()
ide.pack()


win.mainloop()
