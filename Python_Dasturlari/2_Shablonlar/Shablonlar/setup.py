# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='simpletk',
    version='0.4',
    py_modules=['simpletk'],
    requires = ["tkinter"],
    description = "SimpkleTk - simplified tkinter-based framework for GUI design",
    author = "Konstantin Polyakov",
    author_email = "kpolyakov@mail.ru",
    maintainer = "Konstantin Polyakov",
    maintainer_email = "kpolyakov@mail.ru",
    url = "http://kpolyakov.spb.ru/school/probook/python.htm",
    download_url = "http://kpolyakov.spb.ru/school/probook/python.htm",
    keywords = ["application", "framework", "tkinter", "gui", "widget", "builder"],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT licence",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: User Interfaces",
    ],
    license = """
Licensed under MIT licence.
    """,
    long_description = """
SimpleTk tkinter-based framework for GUI design

`SimpleTk` is a **Python3.2+** library designed to enable 
simplified GUI design on the basis of tkinter library.
"""
    )
