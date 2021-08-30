Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    for i,arg in enumerate(args):\n'
 '        print(f"{i}, {arg}")\n')
>>> lines
'def foo(*args):\n    for i,arg in enumerate(args):\n        print(f"{i}, {arg}")\n'
>>> 
= RESTART: G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    for i,arg in enumerate(args):\n'
 '        print(f"{i}, {arg}")\n')
<class 'str'>
>>> print(lines)
def foo(*args):
    for i,arg in enumerate(args):
        print(f"{i}, {arg}")

>>> lines
'def foo(*args):\n    for i,arg in enumerate(args):\n        print(f"{i}, {arg}")\n'
>>> inspect.getargs(foo)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    inspect.getargs(foo)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 1036, in getargs
    raise TypeError('{!r} is not a code object'.format(co))
TypeError: <function foo at 0x0000029653EB5040> is not a code object
>>> inspect.getcallargs(foo)
{'args': ()}
>>> inspect.getcomments(foo)
>>> 
= RESTART: G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    """\n'
 '        foo function does printing using format "i, arg".\n'
 '        Variable i starts from zero.\n'
 '    """\n'
 '    for i,arg in enumerate(args):\n'
 '        # prints from zero to infinity\n'
 '        print(f"{i}, {arg}")\n')
<class 'str'>
>>> 
= RESTART: G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    """\n'
 '        foo function does printing using format "i, arg".\n'
 '        Variable i starts from zero.\n'
 '    """\n'
 '    for i,arg in enumerate(args):\n'
 '        # prints from zero to infinity\n'
 '        print(f"{i}, {arg}")\n')
<class 'str'>
{'args': ()}
None
>>> inspect.getdoc(foo)
'foo function does printing using format "i, arg".\nVariable i starts from zero.'
>>> inspect.getlineno(foo)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    inspect.getlineno(foo)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 1480, in getlineno
    return frame.f_lineno
AttributeError: 'function' object has no attribute 'f_lineno'
>>> inspect.getmembers(foo)
[('__annotations__', {}), ('__call__', <method-wrapper '__call__' of function object at 0x0000020D432970D0>), ('__class__', <class 'function'>), ('__closure__', None), ('__code__', <code object foo at 0x0000020D43245710, file "G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py", line 4>), ('__defaults__', None), ('__delattr__', <method-wrapper '__delattr__' of function object at 0x0000020D432970D0>), ('__dict__', {}), ('__dir__', <built-in method __dir__ of function object at 0x0000020D432970D0>), ('__doc__', '\n        foo function does printing using format "i, arg".\n        Variable i starts from zero.\n    '), ('__eq__', <method-wrapper '__eq__' of function object at 0x0000020D432970D0>), ('__format__', <built-in method __format__ of function object at 0x0000020D432970D0>), ('__ge__', <method-wrapper '__ge__' of function object at 0x0000020D432970D0>), ('__get__', <method-wrapper '__get__' of function object at 0x0000020D432970D0>), ('__getattribute__', <method-wrapper '__getattribute__' of function object at 0x0000020D432970D0>), ('__globals__', {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'G:\\Python Coding\\DeclaringDecorators\\testing getting object source code for functions__from IDLE shell.py', 'inspect': <module 'inspect' from 'C:\\Users\\17033\\AppData\\Local\\Programs\\Python\\Python38\\lib\\inspect.py'>, 'getsource': <function getsource at 0x0000020D42E31820>, 'foo': <function foo at 0x0000020D432970D0>, 'lines': 'def foo(*args):\n    """\n        foo function does printing using format "i, arg".\n        Variable i starts from zero.\n    """\n    for i,arg in enumerate(args):\n        # prints from zero to infinity\n        print(f"{i}, {arg}")\n', 'pprint': <function pprint at 0x0000020D432973A0>}), ('__gt__', <method-wrapper '__gt__' of function object at 0x0000020D432970D0>), ('__hash__', <method-wrapper '__hash__' of function object at 0x0000020D432970D0>), ('__init__', <method-wrapper '__init__' of function object at 0x0000020D432970D0>), ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x00007FFF800B37F0>), ('__kwdefaults__', None), ('__le__', <method-wrapper '__le__' of function object at 0x0000020D432970D0>), ('__lt__', <method-wrapper '__lt__' of function object at 0x0000020D432970D0>), ('__module__', '__main__'), ('__name__', 'foo'), ('__ne__', <method-wrapper '__ne__' of function object at 0x0000020D432970D0>), ('__new__', <built-in method __new__ of type object at 0x00007FFF800B37F0>), ('__qualname__', 'foo'), ('__reduce__', <built-in method __reduce__ of function object at 0x0000020D432970D0>), ('__reduce_ex__', <built-in method __reduce_ex__ of function object at 0x0000020D432970D0>), ('__repr__', <method-wrapper '__repr__' of function object at 0x0000020D432970D0>), ('__setattr__', <method-wrapper '__setattr__' of function object at 0x0000020D432970D0>), ('__sizeof__', <built-in method __sizeof__ of function object at 0x0000020D432970D0>), ('__str__', <method-wrapper '__str__' of function object at 0x0000020D432970D0>), ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x00007FFF800B37F0>)]
>>> inspect.getsourcefile(foo)
'G:\\Python Coding\\DeclaringDecorators\\testing getting object source code for functions__from IDLE shell.py'
>>> 
= RESTART: G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    """\n'
 '        foo function does printing using format "i, arg".\n'
 '        Variable i starts from zero.\n'
 '    """\n'
 '    for i,arg in enumerate(args):\n'
 '        # prints from zero to infinity\n'
 '        print(f"{i}, {arg}")\n')
<class 'str'>
{'args': ()}
None
foo function does printing using format "i, arg".
Variable i starts from zero.
G:\Python Coding\DeclaringDecorators\testing getting object source code for functions__from IDLE shell.py
>>> inspect.getsourcelines(foo)
(['def foo(*args):\n', '    """\n', '        foo function does printing using format "i, arg".\n', '        Variable i starts from zero.\n', '    """\n', '    for i,arg in enumerate(args):\n', '        # prints from zero to infinity\n', '        print(f"{i}, {arg}")\n'], 4)
>>> inspect.signature(foo)
<Signature (*args)>
>>> inspect.getargs(foo)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    inspect.getargs(foo)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 1036, in getargs
    raise TypeError('{!r} is not a code object'.format(co))
TypeError: <function foo at 0x000002296B957040> is not a code object
>>> inspect.findsource(foo)
(['import inspect\n', 'from inspect import getsource\n', '\n', 'def foo(*args):\n', '    """\n', '        foo function does printing using format "i, arg".\n', '        Variable i starts from zero.\n', '    """\n', '    for i,arg in enumerate(args):\n', '        # prints from zero to infinity\n', '        print(f"{i}, {arg}")\n', '\n', 'lines = getsource(foo)\n', 'from pprint import pprint\n', 'pprint(lines)\n', 'print(type(lines))\n', 'print(inspect.getcallargs(foo))\n', 'print(inspect.getcomments(foo))\n', 'print(inspect.getdoc(foo))\n', 'print(inspect.getsourcefile(foo))\n'], 3)
>>> inspect.isfunction(foo)
True
>>> inspect.isclass(foo)
False
>>> 