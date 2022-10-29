REM below requires .pypirc file located under user's home folder to work
REM .pypirc, especially needs to define 
REM [pypi]
REM repository = https://upload.pypi.org/legacy/
REM username = __token__
REM password = ********** (written in plain in the .pypirc)
py -m build
py -m twine upload --repository pypi dist/*