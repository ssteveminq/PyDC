from setuptools import setup
from Cython.Build import cythonize
from setuptools.extension import Extension


sources = [
        "pyddc/pydc.pyx",
        "pyddc/src/dc.cpp",
        "pyddc/src/ddc.cpp",
        "pyddc/src/base.cpp"
]

extension = Extension(
                "pydc",
                sources=sources,
                language="c++",
                include_dirs = ["pydc/include"],
                extra_compile_args = ["-std=c++11"],
                cython_directives={"embedsignature": True},
                libraries = ["Yap"]
)

ext_modules = cythonize([extension], gdb_debug=False)



setup(
        name="PyDC",
        author='Pedro Zuidberg Dos Martires',
        author_email='pedro.zuidbergdosmartires@cs.kuleuven.be',
        url='https://github.com/ML-KULeuven',
        packages=['pyddc'],
        license='Apache 2.0',
        ext_modules = ext_modules,
        zip_safe=False
)