from setuptools import setup, find_packages
import codecs
import os

setup(
    # Application name:
    name="ohbm",

    # Version number:
    version="0.01",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data files
    include_package_data=True,
    zip_safe=False,

    # Details
    url="http://www.github.com/vsoch/ohbm",

    license="LICENSE",
    description="python api wrapper for the ohbm conference.",
    keywords='ohbm,neuroscience,psychology,brains,api,wrapper',

    install_requires = ['numpy','pokemon','requests'],

)
