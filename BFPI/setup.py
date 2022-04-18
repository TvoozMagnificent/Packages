import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="BFPI",
    version="4.0.1",
    description="BFPI: Exactly what it sounds like",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TvoozMagnificent/BrainFuckPlusInterpreter",
    author="TvoozMagnificent",
    author_email="luchang1106@icloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["BFPI"],
    include_package_data=True,
    install_requires=['colorama'],
)


