=============================================================
pyICSParser - ICALENDAR Parser/Validator/Generator/Enumerator
=============================================================

pyICSParser is an icalendar parser/validator/generator/enumerator (for .ics or ical files) as defined 
by RFC5545 (previously RFC2445). 

* Parser returns typed structure
* Validator returns compliance report
* Generator takes typed structures and returns valid icalendar file
* Enumerator returns structure with explicit dates for each instance of event as defined by RRULE, EXRULE, EXDATE, RDATE

Typical usage for Enumerator::

	#!/usr/bin/env python
	from pyICSParser import ical
	mycal = ical.ics()
	mycal.local_load(icsfile)
	mycal.parse_loaded()
	dates = mycal.get_event_instances(start,end)
	#dates will contain the json with all explicit dates of the events spec'ed by the icalendar file

Versions
=========

* Pre-alpha
	-v0.0.1: first pre-alpha
	
	-v0.0.27: fixed the dtstart to dtend problem for holiday

* alpha
	-0.4.x: first fully tested handling days - remains to be done is handling of
	time of events (test vectors are actual icalendar files)
	
	-0.5.x: added support for EXDATE
	
	-0.6.x: added support for DURATION and when DTEND no present, adding support unittest
	
Future developments
--------------------
1. handle of datetime (currently only handles dates)
2. handle of multiple EXRULE,  RRULE as per icalendar spec

Package release
---------------
1. update README.txt

Thanks
-------
* http://pydev.org/updates
* http://www.tele3.cz/jbar/rest/rest.html: reST to HTML & reST validator
* http://guide.python-distribute.org/contributing.html: registering a package on pypi and password information
* http://guide.python-distribute.org/creation.html: uploading a package to pypi
* http://blog.msbbc.co.uk/2007/06/using-googles-free-svn-repository-with.html: how to use google codes, subclipse and eclipse
* http://sphinx-doc.org/tutorial.html