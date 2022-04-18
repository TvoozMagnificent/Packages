# setup.py for package PythonMatrixClass
# use the same setup.py from BFPI

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="PythonMatrixClass",
    version="0.1.0",
    description="PythonMatrixClass module for Python",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TvoozMagnificent/Matrix",
    author="TvoozMagnificent",
    author_email="luchang1106@icloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["PythonMatrixClass"],
    include_package_data=True,
    install_requires=[],
)
