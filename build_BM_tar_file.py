from com_and_decom import com_and_decom as cd
import shutil, os

if __name__ == '__main__':
    name = "black-mamba-1.01.01-linux.tar.gz"
    list_of_files = ["BM_INSTALL", "build", "classes", "CythonModules", "dist",
            "functions", "IDE", "images", "Library", "loop", 'script', "src", 'statement', 'updatingDataBase',
            ".gitignore", ".gitattributes", "PROJECT_DESCRIPTION.md", "BlackMamba.py", "CODE.md", "CONTRIBUTING.md", "LICENSE",
            "mamba.py", "logo.xbm", "README.md"]
    
    path1 = os.path.abspath(os.curdir)+f"/{name}"
    path2 = os.path.abspath(os.curdir)+f"/BM_TAR/{name}"
    cd.compressed(name, list_of_files)
    
    shutil.move(path1, path2)