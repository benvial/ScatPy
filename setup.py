# -*- coding: utf-8 -*-

# from distutils.core import setup
from setuptools import setup, find_packages
from git_version import sdist, get_version
import os.path
import glob


setup(
    name="ScatPy",
    # version=get_version(),
    version="1.0.0",
    author="Andrew G. Mark",
    author_email="mark@is.mpg.de",
    packages=["ScatPy"],
    url="https://github.com/hohlraum/ScatPy",
    platforms="All",
    license="GNU GPLv3",
    description="A Python package for setting up DDSCAT jobs and analysing the results.",
    long_description=open("README.md").read(),
    cmdclass={"sdist": sdist},
    package_data={"ScatPy": ["profiles/*"]},
    package_dir={"ScatPy": "ScatPy"},
    zip_safe=True,
    install_requires=["numpy", "scipy", "matplotlib"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
)
