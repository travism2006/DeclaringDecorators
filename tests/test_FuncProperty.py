from DeclaringDecorators.ExtraDecorator import ExtraDecorator
from DeclaringDecorators.ExtraDecorator import CompDec
from DeclaringDecorators import decscan


#               Basic testsuite
#           Basic test cases go here


# def test_uppercase():
#     assert "loud noises".upper() == "LOUD NOISES"

def test_decoratorCreated():
    test_inst1 = ExtraDecorator()
    assert test_inst1 is not None


def test_compareTwoDecorators():
    test_inst1 = ExtraDecorator("decorator1")
    test_inst2 = ExtraDecorator("decorator2")
    assert test_inst1 != test_inst2


# test case - a decorator name can be changed
def test_decoratorNameChange():
    test_inst1 = ExtraDecorator()
    test_inst1.decoratorName = "MyDecorator1"
    assert test_inst1.decoratorName is not None
    assert test_inst1.decoratorName != ""

# test case - compare the bits to indicate which decorator is smaller or bigger

#               Less Basic testsuite
#           Less basic test cases go here
def test_scanGenericPythonFile():
    results = decscan.decScanFile(r"G:\Python Coding\AutoCreateVirtualEnv.py")
    assert len(results) > 0

# Test binary comparisons
def test_binaryHammingDistance():
    lines = ["@myLog1", "@myLog2"]
    bitsDiff: int = CompDec.findHamDist_BinaryComp(lines[0], lines[1])

    amtDiff = 0
    binDec1 = bin(hash(lines[0]))
    binDec2 = bin(hash(lines[1]))
    binDec1 = binDec1[binDec1.index('b') + 1:]
    binDec2 = binDec2[binDec2.index('b') + 1:]
    for i in zip(binDec1, binDec2):
        if i[0] != i[1]:
            print(i)
            amtDiff += 1

    assert bitsDiff == amtDiff
