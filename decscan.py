from pprint import pprint
# Purpose:
# This part of the module will enable scanning for decorators and properties

def decScanFile(someFilePath: str):
    """
    Scans a given python file and returns a list of data

    @type someFilePath: r-string path for locating decorators and properties within
    @return dataList: list containing number of decorators found, frequency of each decorator
    """

    if not someFilePath.endswith(".py"):
        raise ValueError("File must be a python file to scan for decorators and properties")

    fileLineData = []
    dataDetails = []
    try:
        with open(someFilePath, 'r') as pyFile:
            # if line in pyFile starts with "@" it's a decorator
            for lineNumb, lineData in enumerate(pyFile.readlines()):
                # print(line)
                if "@" in lineData:
                    fileLineData.append(lineData)
                    dataDetails.append(f"line: {lineNumb}, line data: {repr(lineData)}")
    except IOError:
        print("File was not readable. Check file permissions.")
    except ValueError:
        print("someFilePath value is not of type string. Could not open file.")
    except FileNotFoundError:
        print("File was not located.")
    finally:
        return dataDetails


ansList = decScanFile(r"G:\Python Coding\AutoCreateVirtualEnv.py")

pprint(ansList)

try:
    ansList = decScanFile(r"G:\Python Coding")
except ValueError:
    print("Caught value is not a python file.")
finally:
    del ansList
