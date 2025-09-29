"""
antonios takos
Lab 7, accessing data in a file (functions)
Sep 29th, 2025
"""
def testing():
    print("ANTONIOS TAKOS")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)