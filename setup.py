#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
@credit: http://docs.python.org/2/distutils/builtdist.html for setup.py tutorial
@credit: https://github.com/lxml/lxml/blob/master/setup.py for setup.py examples
"""
# from distutils.core import setup
from setuptools import setup

PackageVersion = "0.7.1a3"

setup(
    name = 'pyICSParser',
    version = PackageVersion,
    author = 'Oberron',
    author_email = 'one.annum@gmail.com',
    packages=['pyICSParser'],
    
    
    url = 'http://ical2list.appspot.com',
#     download_url = "https://pypi.python.org/packages/source/p/pyICSParser/pyICSParser-%s.tar.gz"%(PackageVersion),
    license = 'LICENSE.txt',
    keywords = 'iCalendar ical ics parser validator generator events enumerator rfc5545 rfc2445 vcal',
    description='Module supporting the iCalendar specification as defined in RFC5545 as well as its predecessor RFC2445 and non-standard deviances from iCal (Apple), Outlook-calendar (Microsoft), ... ',
    long_description="""\
    pyICSParser is a Python module that provides support for the iCalendar specification as defined in RFC5545.
    
    It aims to be as compatible as possible to iCalendar for its inputs and outputs (RFC5545 strict mode)
    
    Beyond iCalendar strict compatibility is also targets compatibility with RFC2445 (RFC2445-backward compatibility) and with popular calendaring applications (iCal, Outlook, google calendar, ...)
    
    This support includes a Parser, Object Model, Validator, Generator and events instances enumerator for iCalendar files.
    
    In case you want to use the current in-development version, you can get it from the github repository at
    https://github.com/oberron/annum
 """,
    package_dir={'pyICSParser':"./src"},
    classifiers=[
                "Development Status :: 3 - Alpha",
                "Topic :: Utilities",
                "License :: OSI Approved :: BSD License",
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'Programming Language :: Python :: 2.7',
                'Programming Language :: Python :: 3.7',
                "Topic :: Utilities",
    ],
)
