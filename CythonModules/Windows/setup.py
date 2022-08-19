from setuptools import setup, Extension
from Cython.Build import  cythonize



setup(
    name = "my cython modules",
    author='amiehe',
    author_email='amieheessomba@etu.unistra.fr',
    ext_modules=cythonize( 
        [
            "making_stat.pyx", 
            "loop_for.pyx",
            'NumeriCal.pyx',
            'arithmetic_analyze.pyx',
            'fileError.pyx',
            'making_arr.pyx',
            'bm_statistics.pyx',
            'help.pyx',
            'Tuple.pyx',
            'if_statement.pyx'
            ], 
        annotate = True
        )

)
