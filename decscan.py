from pprint import pprint
# Purpose:
# This part of the module will enable scanning for decorators

def decScanFile(path: str):
    """
    Scans a given python file and returns a list of data

    @type path: r-string path for locating decorators within
    @return dataList: list containing number of decorators found, frequency of each decorator
    """
    fileLineData = []
    try:
        with open(path, 'r') as pyFile:
            # if line in pyFile starts with "@" it's a decorator
            for line in pyFile.readlines():
                print(line)
                fileLineData.append(line)
    except ValueError:
        print("path value is not of type string. Could not open file.")
    finally:
        return fileLineData


ansList = decScanFile(r"G:\Python Coding\AutoCreateVirtualEnv.py")

pprint(ansList)
