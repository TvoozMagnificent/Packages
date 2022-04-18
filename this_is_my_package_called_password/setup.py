import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="this_is_my_package_called_password",
    version="2.0.0",
    description="Password validator and generator",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TvoozMagnificent/password",
    author="TvoozMagnificent",
    author_email="luchang1106@icloud.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["this_is_my_package_called_password"],
    include_package_data=True,
    install_requires=[],
)


