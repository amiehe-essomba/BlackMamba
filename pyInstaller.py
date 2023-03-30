import PyInstaller.__main__ 

PyInstaller.__main__.run(
    ["mamba.py",
     '--onefile',
     '--console',
     "-c",
     '--nowindowed',
     ]
)