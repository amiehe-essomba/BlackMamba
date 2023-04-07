from com_and_decom import com_and_decom as cd
import os , sys

def resource_path(relative_path):
    # get absolute path to resource, works for dev and for Pyinstaller
    try:
        # Pyinstaller creates a tem folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def p(relative):
    return os.path.join(
        os.environ.get(
            "_MEI9442",
            os.path.abspath(".")
        ),
        relative
    )
    
if __name__ == '__main__':
    #s, w = resource_path('hello'), p('hello')
    #print(s, '\n', w)
    cd.compressed("BlackMamba.tar.gz", [".vscode", 
                                        "BM_INSTALL", 
                                        "build",
                                        "classes",  
                                        "CythonModules",
                                        "dist", 
                                        "functions",
                                        "IDE",
                                        "images",
                                        "Library",
                                        "loop",
                                        "script",
                                        "src",
                                        "statement",
                                        "updatingDataBase",
                                        ".gitattributes",
                                        ".gitignore",
                                        "BlackMamba.py",
                                        "CODE.md",
                                        "CONTRIBUTING.md",
                                        "LICENSE",
                                        "loggerWriter.py",
                                        "mamba.exe",
                                        "mouse_events.py",
                                        "PROJECT_DESCRIPTION.md",
                                        "README.md",
                                        "setup.py",
                                        "Tools.md",
                                        "WindowsMain.py"
                                        ])
    #path = os.path.abspath(os.curdir)+"\\esso"
    #cd.decompressed("BlackMamba.tar.gz", path)