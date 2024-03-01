from Cython.Build import cythonize
from setuptools import Extension, find_packages, setup

sourcefiles = ["py_shared/square.py"]

extensions = cythonize(Extension(name="py_shared.py_shared", sources=sourcefiles))

kwargs = {"name": "py_shared", "packages": find_packages(), "ext_modules": extensions}

setup(**kwargs)
