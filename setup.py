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
    description='pyICSParser is a Python module that provides support for the iCalendar specification as defined in RFC5545.',
    long_description="""\
    pyICSParser is a Python module that provides support for the iCalendar specification as defined in RFC5545.
    It aims to be as compatible as possible to iCalendar for its inputs and outputs (RFC5545 strict mode, RFC2445-backward compatibility) while targeting compatibility with popular calendaring applications (iCal, Outlook, google calendar, ...)
    This support includes a Parser, Object Model, Validator, Generator and events instances enumerator for iCalendar files.
 """,
    package_dir={'pyICSParser':".\src"},
    classifiers=[
                "Development Status :: 3 - Alpha",
                "Topic :: Utilities",
                "License :: OSI Approved :: BSD License",
                'Environment :: Console',
                'Intended Audience :: End Users/Desktop',
                'Intended Audience :: Developers'
                'Operating System :: MacOS :: MacOS X',
                'Operating System :: Microsoft :: Windows',
                'Programming Language :: Python :: 2.4',
                'Programming Language :: Python :: 2.5',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
    ],
)
