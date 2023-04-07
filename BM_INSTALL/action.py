from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox , filedialog
from BM_INSTALL import right_frame
from BM_INSTALL import unzip_and_compress as unzip
from BM_INSTALL import unstall
from BM_INSTALL import check_if_bm_is_installed as cbm
from BM_INSTALL import scroll_bar
import os 
import shutil


def action( frame1, frame2, root,  main_root, ico_path, license ):
    List = ['Install BLACK MAMBA', "Uninstall BLACK MAMBA", "Repair BLACK MAMBA"]
    height = 40
    frame0 =  LabelFrame(root,  bd = 5, width=390, height=150, relief=FLAT, text="BLACK MAMBA PROGRAMM INSTALLATION",
                         font=("calibri",10, 'bold'), bg='white')
    frame1 =  Frame(root,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame2 =  Frame(root,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame3 =  Frame(root,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    
    frame0.place(x=0, y=0, width=390, height=150 )
    frame1.place(x=0, y=150, width=300, height=height )
    frame2.place(x=0, y=200, width=300, height=height )
    frame3.place(x=0, y=250, width=300, height=height )
    
    _scroll_bar_ = scroll_bar.scroll_bar(frame0, " ")
    
    label1 = Button(frame1, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue',  
        width=50, height=50,  relief=GROOVE, anchor='w', command = lambda : installation(frame1, frame2, root, main_root, ico_path, frame0, license) )
    label2 = Button(frame2, text=List[1], font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
                    width=50, height=50,  relief=GROOVE, anchor='w', command = lambda : uninstall_bm(frame1, frame2, root, main_root, ico_path))
    label3 = Button(frame3, text=List[2], font=("calibri", 10, 'bold', 'underline'), foreground='blue', width=50, height=50,  relief=GROOVE, anchor='w')
    
    label1.pack() 
    label2.pack() 
    label3.pack() 
    
    
def back(frame1, frame2, root, main_root, ico_path, root_path,  frame0, license): 
    global check_bnt_int
    
    height = 40
    List = ['Select location']
    FRAME = Frame(main_root, relief=RAISED, bd = 4, width=400, height=350, bg='white')
    FRAME.place(x=200, y=0)
    FRAME0 = Frame(main_root, relief=RAISED, bd = 4, width=400, height=50, bg='white')
    FRAME0.place(x=200, y=360)
    
    frame0 =  LabelFrame(FRAME,  bd = 5, width=390, height=150, relief=FLAT, text="BLACK MAMBA PROGRAMM INSTALLATION",
                         font=("calibri",10, 'bold'), bg='white')
    frame1 =  Frame(FRAME,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame2 =  Frame(FRAME,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame3 =  Frame(FRAME,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame4 =  Frame(FRAME,  bd = 5, width=390, height=height, relief=FLAT,  bg='white')
    frame0.place(x=0, y=0, width=390, height=150 )
    frame1.place(x=0, y=150, width=300, height=height)
    frame2.place(x=0, y=190, width=300, height=height)
    frame3.place(x=0, y=230, width=300, height=height)
    frame4.place(x=0, y=270, width=300, height=height)
    
    _scroll_bar_ = scroll_bar.scroll_bar(frame0, " ")
    
    data = [FRAME0, root_path, frame4]
    label1 = Button(frame1, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue',
            width=50, height=50,  relief=GROOVE, anchor='w', command=lambda : dialog(frame2, frame3, data, main_root))
    label1.pack()
    
    install_btn = Button(FRAME0, text='install', state=DISABLED, width=10, relief=GROOVE, 
                         command=lambda : unzip.unzip_file(root_path, read_location(), frame4))
    install_btn.place(x=0, y=4)
    
    prev_btn = Button(FRAME0, text='previous', state=NORMAL, width=10, relief=GROOVE, 
                    command=lambda : right_frame.nex_section(FRAME, FRAME0, root, main_root, ico_path, license ))
    prev_btn.place(x=85, y=4)
    
def installation(frame1, frame2, root, main_root, ico_path, frame0, license):
    _scroll_bar_ = scroll_bar.scroll_bar(frame0, " ")
    root_path    = os.path.abspath(os.curdir)
    back(frame1, frame2, root, main_root, ico_path, root_path, frame0, license)
    
    
def uninstall_bm(frame1, frame2, root, main_root, ico_path):
    btn, label, frame = unstall.unstall_new_window(frame1, frame2, root, main_root, ico_path)
    btn.config(state=DISABLED)
    
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
    __path = root_path+"\\BM_INSTALL\\"
    os.path.join( os.environ.get( "_MEI9442",  __path), "" )
    list_dir = os.listdir( __path)
    if __path__root:
        if __path__root :
            if name in list_dir: 
                __path__ = root_path+f"\\BM_INSTALL\\{name}\\"
                os.path.join( os.environ.get( "_MEI9442",  __path__), "" )
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
        
        if os.path.isdir(__path__root) is True:
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
            check_bnt = Checkbutton(frame_, text='activation', variable=check_bnt_int, onvalue=1,offvalue=0, selectcolor='ivory', 
                            command=lambda : key_activation(check_bnt_int,  data[0], data[1], data[2], main_root)) 
            check_bnt.place(x=0, y=0)
        else: print(".......................................")
    else: pass

def key_activation(value, frame, root_path, progress_bar_frame,  main_root):
    if value.get() == 1: 
        install_btn = Button(frame, text='install', state=NORMAL, width=10, relief=GROOVE, 
                             command=lambda : unzip.unzip_file(root_path, read_location(), progress_bar_frame, main_root)) 
        install_btn.place(x=0, y=4)
    else: 
        install_btn = Button(frame, text='install', state=DISABLED, width=10, relief=GROOVE,
                             command=lambda : unzip.unzip_file(root_path, read_location(), progress_bar_frame, main_root)) 
        install_btn.place(x=0, y=4)

def read_location():
    path = os.path.abspath(os.curdir)+"\\BM_INSTALL\\black_mamba_location\\path.bm"
    line=""
    with open(path, 'r') as f:
        line = f.readline().rstrip()
    f.close()
    
    return line

