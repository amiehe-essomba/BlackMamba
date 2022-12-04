from distutils.core import setup 
from Cython.Build import cythonize
from distutils.extension import Extension 
from Cython.Distutils import build_ext 

ext_modules = [
    Extension('tuple',
            ["Tuple.pyx"],
            libraries=['loop'],
            extra_compile_args=['/openmp'],
            extra_link_args=['/openmp'],
        
            )
]

setup(
    name='tuple',
    cmdclass={'build_ext' : build_ext},
    ext_modules=ext_modules
)
