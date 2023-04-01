import tarfile
import os 
from tkinter.ttk    import *
from tkinter        import *
import time
from BM_INSTALL     import commands as cmd
from tqdm import tqdm


def unzip_file(path, path_destination_folder, frame, main_root, destroy_install, root, frame_ ):
    #new_path = path+"\\BM_INSTALL\\black-mamba-1.01.01-win64.tar.gz"
    new_path = path+"\\BM_INSTALL\\file.tar.gz"
    ######
    style = Style()
    style.theme_use('default')#'clam'
    style.configure('red.Horizontal.TProgressbar',background='blue')

    progress = Progressbar(frame, length=180, orient= HORIZONTAL, mode='determinate', 
    style='red.Horizontal.TProgressbar')
    progress.place(x=0, y=0)
    
    with tarfile.open(new_path) as file:
        t_len = len(file.getmembers())
        N = (100 / t_len)
        M = 0
        for member in tqdm(iterable=file.getmembers(), total=len(file.getmembers())):
            file.extractall(f"{path_destination_folder}")
            M += 1
            N *= M 
            main_root.update_idletasks()
            progress['value'] += N
            time.sleep(0.001)
            Label(frame, text=str(int(progress['value']))+'%',width=5, font = ('Arial', 12),
            foreground='black').place(x=190, y=0)
            
        entree = Entry(frame,  font=('arial', 10, 'bold'), width=50) 
        entree.place(x=190, y=0, width = 50)
        entree.insert(0, '')
        entree.delete(0, END)
        entree.insert(0,'Done !')
        entree.config(state=DISABLED,bg='ivory')
        
        progress_bar(frame, main_root, destroy_install, root)
    file.close()
    
    new_path = path+"\\BM_INSTALL\\black_mamba_location\\install.bm"
    
    with open(new_path, "w") as f:
        f.write('Done')
    f.close()
        
def progress_bar(frame, main_root, destroy_install, root, bool=False):
    destroy_install.destroy()
    destroy_install =  Frame(root, relief=FLAT,  width=390, height=50, background='white')
    destroy_install.place(x=0, y=360, width=390, height=40)
    
    break_button = Button(destroy_install, text='cancel', state=NORMAL, width=10, relief=GROOVE, command= lambda : destroy_root(main_root))
    break_button.place(x=280, y=4)
    
    List = ['Select location']
    frame_2 =  Frame(root,  bd = 5, width=390, height=50, relief=FLAT, bg="white")
    frame_2.place(x=5.5, y=168, width=300, height=40 )
    frame_3 =  Frame(root,  bd = 5, width=390, height=50, relief=FLAT, bg="white")
    frame_3.place(x=5.5, y=248, width=300, height=40 )
    
    label1 = Button(frame_2, text=List[0], font=("calibri", 10, 'bold', 'underline'), foreground='blue', 
            width=50, height=50,  relief=GROOVE, anchor='w', state=DISABLED)
    label1.pack()
    
    check_bnt_int = IntVar()
    check_bnt_int.set(1)

    check_bnt = Checkbutton(frame_3, text='activation', variable=check_bnt_int,  
                    onvalue=1,offvalue=0, selectcolor='ivory', state=DISABLED) 
    check_bnt.place(x=0, y=0)
    
def destroy_root(root):
    root.destroy()
    