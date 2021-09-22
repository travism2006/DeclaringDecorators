from inspect import getsource


def decIter(funcObj):
    """
        Takes a decorator function object and returns an iterable of the line-by-line source code/definition.
    """
    temp1 = getsource(funcObj).strip().split("\n")
    # temp2 = inspect.findsource(funcObj) #-----DO NOT USE METHOD findsource(function)
    from pprint import pprint
    print(temp1)
    print(type(temp1))
    return temp1


# def mymain():
#     """Normal input for testing generic numerical function object"""
#
#     def mySum(a: int, b: int):
#         return a + b
#
#     myIter = decIter(mySum)
#
#
# mymain()
