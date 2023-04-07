import PyInstaller.__main__ 
import os

def ico_path():
    # ico image path
    system  = "Linux"
    if system == 'Linux':
        return os.path.abspath(os.curdir)+'\\images\\logo.ico'
    else:  return None 
    
path  =  os.path.abspath(os.curdir)+"\\images\\*;."

PyInstaller.__main__.run(
    ["black-mamba-1.01.01-win64.py",
     '--onefile',
     '--console',
     "-c",
     "--clean",
     '--nowindowed',
     f'--icon={ico_path()}',
     f'--add-data={path}'
     ]
)
