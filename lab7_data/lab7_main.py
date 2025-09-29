"""
antonios takos
Lab 7, accessing data in a file
Sep 29th, 2025
"""
from lab7_function import *

testing()
print("\n ---- example 1: reading file -----")
with open('phrases.txt', 'r') as fileuser:
    eachline = fileuser.readlines()
    print(eachline)