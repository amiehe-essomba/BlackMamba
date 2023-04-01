from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox , filedialog
from BM_INSTALL import right_frame
from BM_INSTALL import unzip_and_compress as unzip
from BM_INSTALL import unstall
from BM_INSTALL import check_if_bm_is_installed as cbm
import os 
import shutil


def action( frame1, frame2, root,  main_root, ico_path ):
    List = ['Install BLACK MAMBA', "Uninstall BLACK MAMBA", "Repair BLACK MAMBA"]
    frame0 =  LabelFrame(root,  bd = 5, width=390, height=150, relief=FLAT, text="BLACK MAMBA PROGRAMM INSTALLATION",
                         font=("calibri",10, 'bold'), bg='white')
    frame1 =  Frame(root,  bd = 5, width=390, height=50, relief=FLAT,  bg='white')
    frame2 =  Frame(root,  bd = 5, width=390, height=50, relief=FLAT,  bg='white')
    frame3 =  Frame(root,  bd = 5, width=390, height=50, relief=FLAT,  bg='white')
    
    frame0.place(x=0, y=0, width=390, height=150 )
    frame1.place(x=0, y=150, width=300, height=50  )
    frame2.place(x=0, y=210, width=300, height=50 )
    frame3.place(x=0, y=270, width=300, height=50 )
    
    label1 = Button(frame1, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue',  
        width=50, height=50,  relief=GROOVE, anchor='w', command = lambda : installation(frame1, frame2, root, main_root, ico_path) )
    label2 = Button(frame2, text=List[1], font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
                    width=50, height=50,  relief=GROOVE, anchor='w', command = lambda : uninstall_bm(frame1, frame2, root, main_root, ico_path))
    label3 = Button(frame3, text=List[2], font=("calibri", 10, 'bold', 'underline'), foreground='blue', width=50, height=50,  relief=GROOVE, anchor='w')
    
    label1.pack() 
    label2.pack() 
    label3.pack() 
    
    
def back(frame1, frame2, root, main_root, ico_path, root_path, location): 
    global check_bnt_int
    
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
    
    data = [frame2, root_path, location, frame_4, root, frame1]
    label1 = Button(frame_1, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
            width=50, height=50,  relief=GROOVE, anchor='w', command=lambda : dialog(frame_2, frame_3, data, main_root))
    label1.pack()
    
    install_btn = Button(frame2, text='install', state=DISABLED, width=10, relief=GROOVE, 
                         command=lambda : unzip.unzip_file(root_path, read_location(), frame_4))
    install_btn.place(x=0, y=0)
    
    prev_btn = Button(frame2, text='previous', state=NORMAL, width=10, relief=GROOVE, 
                    command=lambda : right_frame.nex_section(frame1, frame2, root, main_root, ico_path ))
    prev_btn.place(x=85, y=0)
    
def installation(frame1, frame2, root, main_root, ico_path):
    root_path    = os.path.abspath(os.curdir)
    back(frame1, frame2, root, main_root, ico_path, root_path, "")
    
def uninstall_bm(frame1, frame2, root, main_root, ico_path):
    btn, label, frame = unstall.unstall_new_window(frame1, frame2, root, main_root, ico_path)
    btn.config(state=DISABLED)
    
    #label = Button(frame, text="", font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
    #        width=50, height=50,  relief=GROOVE, anchor='w' )
    #label.pack()
    try:
        root_path  = cbm.mamba()
        if type(root_path) == type(str()):
            shutil.rmtree(root_path+"\\esso") 
        else: pass
        
        entree = Entry(frame,  font=('arial', 10, 'bold'), foreground='blue', width=50 ) 
        entree.pack()
        entree.insert(0, '')
        entree.delete(0, END)
        entree.insert(0,'Complete unstallation !')
        entree.config(state=DISABLED, bg='ivory')
    
    except FileNotFoundError: 
        entree = Entry(frame,  font=('arial', 10, 'bold'), foreground='blue', width=50 ) 
        entree.pack()
        entree.insert(0, '')
        entree.delete(0, END)
        entree.insert(0,'Black Mamba is not already installed !')
        entree.config(state=DISABLED, bg='ivory')
    
def dialog(frame, frame_, data, main_root):   
    __path__root = filedialog.askdirectory()
    root_path    = os.path.abspath(os.curdir)
    name = 'black_mamba_location'
    list_dir = os.listdir(root_path+"\\BM_INSTALL\\")
    if __path__root :
        if name in list_dir: 
            direct_access = root_path+f"\\BM_INSTALL\\{name}\\path.bm"
            with open(direct_access, 'w') as f:
                f.write(f'{__path__root}')
            f.close()
        else:
            path_new = root_path+f"\\BM_INSTALL\\{name}\\"
            os.mkdir(path_new)
            direct_access = root_path+f"\\BM_INSTALL\\{name}\\path.bm"
            with open(direct_access, 'w') as f:
                f.write(f'{__path__root}')
            f.close()
    else: pass
    
    label = Label(frame, text='PATH', anchor='w')
    label.place(x=0, y=0, width=300, height=30)   
    
    entree = Entry(frame, relief=GROOVE, bg='white', font=('arial', 10, 'bold', 'underline')) 
    entree.place(x=50, y=0, width=300, height=30 )
    entree.insert(0, '')
    entree.delete(0, END)
    entree.insert(0, f"{__path__root}")
    entree.config(state=DISABLED)
    
    check_bnt_int = IntVar()
    check_bnt_int.set(0)
    
    #data = [frame, root_path, location] refering  to key_activation
    #data[0] = frame1 = frame
    #data[5] = frame2 = frame_
    #data[4] = root
    check_bnt = Checkbutton(frame_, text='activation', variable=check_bnt_int,  
                    onvalue=1,offvalue=0, selectcolor='ivory', command=lambda : key_activation(check_bnt_int, 
                                                data[0], data[1], data[2], data[3], main_root, data[4], data[5])) 
    check_bnt.place(x=0, y=0)

def key_activation(value, frame, root_path, location, progress_bar_frame,  main_root, root, frame_):
    if value.get() == 1: 
        install_btn = Button(frame, text='install', state=NORMAL, width=10, relief=GROOVE, 
                             command=lambda : unzip.unzip_file(root_path, read_location(), progress_bar_frame, main_root, frame, root, frame_=frame_))
        install_btn.place(x=0, y=0)
    else: 
        install_btn = Button(frame, text='install', state=DISABLED, width=10, relief=GROOVE,
                             command=lambda : unzip.unzip_file(root_path, read_location(), progress_bar_frame, main_root, frame, root, frame_))
        install_btn.place(x=0, y=0)

def read_location():
    path = os.path.abspath(os.curdir)+"\\BM_INSTALL\\black_mamba_location\\path.bm"
    line=""
    with open(path, 'r') as f:
        line = f.readline().rstrip()
    f.close()
    
    return line

