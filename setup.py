# -*- coding:utf-8 -*-
"""
Created on Jan 6, 2012

@author: Oberron
"""
from distutils.core import setup

setup(
    name = 'pyICSParser',
    version = '0.6.2a1',
    author = 'Oberron',
    author_email = 'one.annum@gmail.com',
    packages=['pyICSParser'],
    scripts=['rsc/utest/u_icalendar.py','rsc/utest/test_vect.py','rsc/utest/u_dateutil_rrul.py'],
    url = 'http://ical2list.appspot.com',
    license = 'LICENSE.txt',
    keywords = 'iCalendar ical ics parser validator generator events enumerator rfc5545 rfc2445 vcal',
    description='iCalendar parser, validator, generator, events enumerator',
    long_description='README.txt',
    package_dir={'pyICSParser':".\src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
