import inspect
from inspect import getsource

def foo(*args):
    for i,arg in enumerate(args):
        print(f"{i}, {arg}")

lines = getsource(foo)
from pprint import pprint
pprint(lines)
