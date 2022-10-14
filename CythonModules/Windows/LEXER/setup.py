from setuptools import setup, Extension
from Cython.Build import  cythonize



setup(
    name = "my cython modules",
    author='amiehe',
    author_email='amieheessomba@etu.unistra.fr',
    ext_modules=cythonize( 
        [
            "comment_line.pyx", 
            "checking_tabulation.pyx",
            "checking_if_affectation.pyx",
            "Dictionary.pyx",
            "float_or_function.pyx"
            ], 
        annotate = True
        )

)
