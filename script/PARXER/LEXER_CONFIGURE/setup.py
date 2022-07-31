from setuptools import setup, Extension
from Cython.Build import  cythonize


setup(
    name = "loop for",
    author='amiehe',
    author_email='amieheessomba@etu.unistra.fr',
    ext_modules=cythonize(
        ["making_stat.pyx", 
            "loop_for.pyx"]
        )
)
