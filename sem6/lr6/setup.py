from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(
        "ferma_fact.pyx",
        annotate=True,
        compiler_directives={"language_level": "3"}
    )
)

