import PyInstaller.__main__ 
import os
from BM_ERRORS    import errors

def path_ico():
    # get ico image 
    error  = None 
    
    system  = os.uname()[0]
    if system == "Linux":
        return os.path.abspath(os.curdir)+"/images/logo.ico"
    else: error =  errors.mamba_error().ERROR1(system)

path = path_ico()
if path is None: print(path)
else:
    data = os.path.abspath(os.curdir)+'/Library/*;.'
    data_info = os.path.abspath(os.curdir)+'/README.md;CONTRIBUTING.md;Tools.md;CODE.md'
    PyInstaller.__main__.run([
        "mamba.py",
        '--onefile',
        '--console',
        '-c',
        '--clean',
        '--nowindowed',
        f"--icon={path}",   
    ])
    