#!/usr/bin/env python

from __future__ import print_function

string1 = "John"
string2 = "Jane"
string3 = "Jim"

try:
    # PY2
    string4 = raw_input("Enter fourth name: ")
except NameError:
    # PY3
    string4 = input("Enter fourth name: ")

print()
print("{:<20}".format(string1))
print("{:<20}".format(string2))
print("{:<20}".format(string3))
print("{:<20}".format(string4))
