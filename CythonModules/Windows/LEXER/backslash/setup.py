from setuptools import setup, Extension
from Cython.Build import  cythonize



setup(
    name = "my cython modules",
    author='amiehe',
    author_email='amieheessomba@etu.unistra.fr',
    ext_modules=cythonize( 
        [
            "bs_deep_checking.pyx", 
            "checking_if_backslash.pyx",
            ], 
        annotate = False
        )
)