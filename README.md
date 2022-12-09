# Test Automation Scripts

These are test automation scipts running on python.
They test elements, URL loading and element attributes on https://profilence.com/.

The scripts were written with selenium 4.7.0 and Python 3.10.6.
4 of the tests(excluding testSwiperElement.py), are run from command-line interface, with the command:
py script-name.py

Usage example:
  py loadBlogArticle.py
  
testSwiperElement.py is run with an optional argument which is a floating-point number greater than zero.
Usage:
  py testSwiperElement.py 1.0

On error, these scripts raise AssertionError. They return nothing on succesful testing.
