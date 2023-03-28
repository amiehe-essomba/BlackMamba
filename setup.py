import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["idna"], "excludes": ["tkinter"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None

packages = ['idna']# ['os']#['idna']
options = {
    'build_exe': {
        'packages' : packages,
    }
}

if sys.platform == "win32"  : base = "Win32GUI"
elif sys.platform == 'Linux': base = 'Linux'
else: pass

executables = [Executable("mamba.py", base = base)]

setup(
    name="mamba",
    version="1.0.0",
    description="Black Mamba programming language",
    options=options,#{"build_exe": build_exe_options},
    executables=executables,# [Executable("guifoo.py", base=base)],
    )
