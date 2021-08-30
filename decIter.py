import inspect
from inspect import getsource
from inspect import findsource


def decIter(funcObj):
    """
        Takes a decorator function object and returns an iterable of the line-by-line source code/definition.
    """
    # temp1 = getsource(funcObj)
    temp2 = inspect.findsource(funcObj)
    from pprint import pprint
    pprint(temp2)
    print(type(temp2))
    return temp2


def mymain():
    """Normal input for testing generic numerical function object"""

    def mySum(a: int, b: int):
        return a + b

    # res = mySum(0, 1)
    myIter = decIter(mySum)


mymain()
