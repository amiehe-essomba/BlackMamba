from setuptools import setup, Extension
from Cython.Build import  cythonize



setup(
    name = "my cython modules",
    author='amiehe',
    author_email='amieheessomba@etu.unistra.fr',
    ext_modules=cythonize( 
        [
            "segmentation.pyx", 
            "num.pyx",
            'segError.pyx',
            'characters.pyx',
            'subString.pyx',
            'seg_Interpretor.pyx'
            ], 
        annotate = False
        )

)
