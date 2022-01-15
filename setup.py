#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
@credit: http://docs.python.org/2/distutils/builtdist.html for setup.py tutorial
@credit: https://github.com/lxml/lxml/blob/master/setup.py for setup.py examples
"""
# from distutils.core import setup
from setuptools import find_packages, setup
from glob import glob
with open("README.md", "r", encoding="utf-8") as fi:
    long_description = fi.read()
PackageVersion = "0.7.2a2"
setup(
    name = 'pyICSParser',
    version = PackageVersion,
    author = 'Oberron',
    author_email = 'one.annum@gmail.com',
    description='Module supporting the iCalendar specification as defined in RFC5545 as well as its predecessor RFC2445 and non-standard deviances from iCal (Apple), Outlook-calendar (Microsoft), ... ',
    long_description=long_description,
    long_description_content_type="text/markdown",

    
    
    url = 'http://ical2list.appspot.com',
    project_urls={
        "Bug Tracker": "https://github.com/1-annum/pyICSParser/issues",
    },
#     download_url = "https://pypi.python.org/packages/source/p/pyICSParser/pyICSParser-%s.tar.gz"%(PackageVersion),
    license = 'LICENSE.txt',
    keywords = 'iCalendar ical ics parser validator generator events enumerator rfc5545 rfc2445 vcal',
    
    packages=['pyICSParser'],
    package_dir={'pyICSParser':"./src"},
    classifiers=[
                "Development Status :: 3 - Alpha",
                "Topic :: Utilities",
                "License :: OSI Approved :: BSD License",
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: Developers',
                "Operating System :: OS Independent",
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.7',
                "Topic :: Utilities",
    ],
)
