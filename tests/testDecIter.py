from DeclaringDecorators.decIter import decIter

def test_decoratorIterator():
    """Normal input for testing generic numerical function object"""
    def mySum(a: int, b: int):
        return a+b
    listOfLines = decIter(mySum)
    assert listOfLines is not None

def test_decoratorIteratorTwo():
    def mySum(a: int, b: int):
        return a+b
    listOfLines = decIter(mySum)
    assert len(listOfLines) > 0

#########################
#    invalid test case  #
#########################
    """None provided as input for some generic numerical function obj"""
    # def myDiff(a: int, b: int):
    #     return a-b
    # otherIter = decIter(myDiff(None, 4))
