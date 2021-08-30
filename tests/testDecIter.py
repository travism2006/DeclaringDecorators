from DeclaringDecorators.decIter import decIter

def test_decoratorIterator():
    """Normal input for testing generic numerical function object"""
    def mySum(a: int, b: int):
        return a+b
    myIter = decIter(mySum(0, 1))

    """None provided as input for some generic numerical function obj"""
    # def myDiff(a: int, b: int):
    #     return a-b
    # otherIter = decIter(myDiff(None, 4))
