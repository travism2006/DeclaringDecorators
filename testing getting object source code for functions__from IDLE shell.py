import inspect
from inspect import getsource

def foo(*args):
    """
        foo function does printing using format "i, arg".
        Variable i starts from zero.
    """
    for i,arg in enumerate(args):
        # prints from zero to infinity
        print(f"{i}, {arg}")

lines = getsource(foo)
from pprint import pprint
#pprint(lines)
t1 = type(lines)
t2 = inspect.getcallargs(foo)
t3 = inspect.getcomments(foo)
t4 = inspect.getdoc(foo)
t5 = inspect.getsourcefile(foo)
t6 = inspect.getsourcelines(foo)
t7 = inspect.findsource(foo)
###
#print('type(lines): ', t1)
#print("inspect.getcallargs(foo): ", t2)
#print('inspect.getcomments(foo): ', t3)
#print('inspect.getdoc(foo): ', t4)
#print('inspect.getsourcefile(foo): ', t5)
#pprint(f'inspect.getsourcelines(foo): {t6}')
print(type(t6))
pprint(f'inspect.findsource(foo): {t7}')
print(type(t7))
