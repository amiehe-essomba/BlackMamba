from tkinter import *
from tkinter import messagebox 
from BM_INSTALL import action


def sel( value, frame1, frame2, root,  main_root, ico_path, license ):        
    if value.get() == 1: 
        next_btn = Button(frame2, text='next', state=NORMAL, width=9, relief=GROOVE, 
                command=lambda: nex_section(frame1=frame1, frame2=frame2, root=root, main_root=main_root, ico_path=ico_path, license=license))
        next_btn.place(x=75, y=0)
    else:
        nex_btn = Button(frame2, text='next', state=DISABLED, width=9, relief=GROOVE)
        nex_btn.place(x=75, y=0)
    
    prev_btn = Button(frame2, text='previous', state=DISABLED, width=9, relief=GROOVE)
    prev_btn.place(x=180, y=0)
    
def nex_section(frame1, frame2,  root, main_root, ico_path,license):
    frame1.destroy()
    frame2.destroy()
    
    frame1 = LabelFrame(root, relief=FLAT, bd = 5, width=390, height=350, 
                            text='BLACK MAMBA PROGRAMM INSTALLATION', font=("calibri", 10, 'bold'), bg='white')
    frame2 =  Frame(root, relief=FLAT, bd = 5, width=390, height=50,  bg='white')
    frame1.place(x=0, y=0, width=390, height=350) 
    frame2.place(x=0, y=360, width=390, height=50)
    
    action.action(frame1, frame2,  root, main_root, ico_path, license)
    
    prev_btn = Button(frame2, text='next', state=DISABLED, width=9, relief=GROOVE)
    prev_btn.place(x=0, y=0)
    prev_btn = Button(frame2, text='previous', state=NORMAL, width=9, relief=GROOVE, 
                    command=lambda : scrollbar_right(frame_right=root, main_root=main_root, ico_path=ico_path, license=license))
    prev_btn.place(x=100, y=0)
    
    right(ico_path=ico_path, main_root=main_root).cancel(root=frame2)
    
def scrollbar_right(frame_right, main_root, ico_path, license):
    sub_frame_right1 =  LabelFrame(frame_right, relief=FLAT, bd = 5, width=390, height=350, 
                            text='BLACK MAMBA LICENSE', font=("calibri", 10, 'bold'))
    sub_frame_right2 =  Frame(frame_right, relief=FLAT, bd = 5, width=390, height=40)    
    
    sub_frame_right1.place(x=0, y=0, width=390, height=350) 
    sub_frame_right2.place(x=0, y=360, width=390, height=40) 
    
    scrollbar_v = Scrollbar(sub_frame_right1, orient=VERTICAL)
    scrollbar_v.pack(side=RIGHT, fill=BOTH, ipady=5)
    
    scrollbar_h =  Scrollbar(sub_frame_right1, orient=HORIZONTAL)
    scrollbar_h.pack(fill=BOTH, side=BOTTOM, ipadx=5)
    
    my_list = Listbox(sub_frame_right1, yscrollcommand=scrollbar_v.set, xscrollcommand=scrollbar_h.set)
    for s in license:
        my_list.insert(END, s)
    my_list.pack(fill=BOTH, expand=YES)
    
    scrollbar_v.config(command=my_list.yview)
    scrollbar_h.config(command=my_list.xview)
    
    get_var = IntVar()    
    agree = Checkbutton(sub_frame_right2, text='agree', variable=get_var, onvalue=1,offvalue=0, 
                    selectcolor='ivory', command=lambda : sel(value=get_var, frame1=sub_frame_right1, 
                    frame2=sub_frame_right2, root=frame_right, main_root=main_root, ico_path=ico_path,license=license ))
    agree.place(x=0, y=0)
       
    next_ = Button(sub_frame_right2, text='next', state=DISABLED, width=9, relief=GROOVE)
    next_.place(x=75, y=0)
    
    prev_btn = Button(sub_frame_right2, text='previous', state=DISABLED, width=9, relief=GROOVE)
    prev_btn.place(x=180, y=0)
    
    return sub_frame_right2

class right:
    def __init__(self, ico_path, main_root) :
        self.ico_path = ico_path
        self.main_root = main_root
        
    def cancel(self, root):
        self.cancel = Button(root, width=10, text='cancel', command =  lambda : right(self.ico_path, self.main_root).destroy_root(root, 
                                                        self.main_root), state=NORMAL, relief=GROOVE)
        self.cancel.place(x=280, y=0)
    
    def destroy_root( self, root,  main_root ):    
        def yes(root1, root2, root3):
            root1.destroy()
            root2.destroy()
            root3.destroy()
        
        def no(root):
            root.destroy()
            
        self.width, self.height, self.max = 300, 120, 30
        self.sub_root = Tk()
        self.sub_root.title("Black Mamba 1.01.01 64-bit")
        self.sub_root.geometry(f"{self.width}x{self.height}")
        self.sub_root.minsize(self.width, self.height)
        self.sub_root.maxsize(self.width, self.height)
        self.sub_root.config()
        root_menu = Menu(self.sub_root)
        self.sub_root.iconbitmap('@logo.xbm')#self.ico_path)
        self.sub_root.resizable(width=True, height=True)
        
        F1 = Frame(self.sub_root, relief=FLAT,  width=self.width, height=self.height-self.max)
        F1.pack(expand=YES)
        
        F2 = Frame(self.sub_root, relief=FLAT, width=self.width, height=self.max)
        F2.pack(expand=YES)
        
        label = Label(F1, text="are you sure you want to cancel ?", font=('Arial', 12, "italic"), foreground='black')
        label.pack()
        
        self.no = Button(F2, text='yes', width=9, command = lambda : yes(self.sub_root, root, main_root), state=NORMAL,  relief=GROOVE)
        self.no.place(x=50, y=0)
        
        self.yes = Button(F2, text='no', width=9, command = lambda : no(self.sub_root), state=NORMAL, relief=GROOVE)
        self.yes.place(x=160, y=0)