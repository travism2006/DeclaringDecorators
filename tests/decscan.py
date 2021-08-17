# Purpose:
# This part of the module will enable scanning for decorators
# import os

def decScanFile(path: str):
    """
    Scans a given python file and returns a list of data

    @type path: r-string path for locating decorators within
    @return dataList: list containing number of decorators found, frequency of each decorator
    """

    try:
        with open(path, 'r') as pyFile:
            # if line in pyFile starts with "@" it's a decorator
            for line in pyFile.readlines():
                print(line)
    except ValueError:
        print("path value is not of type string. Could not open file.")
