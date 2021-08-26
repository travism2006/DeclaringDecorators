Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def bar(*args):
	for i, ar in enumerate(args):
		print(i, ', ', ar)

		
>>> bar
<function bar at 0x0000023674CC7040>
>>> bar.__annotations__
{}
>>> bar.__code__
<code object bar at 0x0000023674CCE710, file "<pyshell#4>", line 1>
>>> bar.__dict__
{}
>>> bar.__doc__
>>> def foo(a: str):
	"""
	A name is provided and printed to the user
	"""
	print(f"Hello {a}")
	return a

>>> foo.__annotations__
{'a': <class 'str'>}
>>> foo.__call__
<method-wrapper '__call__' of function object at 0x0000023674CF04C0>
>>> foo.__class__
<class 'function'>
>>> foo.__code__
<code object foo at 0x0000023674CCEBE0, file "<pyshell#16>", line 1>

>>> foo.__dict__
{}
>>> foo.__doc__
'\n\tA name is provided and printed to the user\n\t'
>>> foo.__getattribute__
<method-wrapper '__getattribute__' of function object at 0x0000023674CF04C0>
>>> 
>>> 
>>> 
>>> foo.__globals__
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'bar': <function bar at 0x0000023674CC7040>, 'foo': <function foo at 0x0000023674CF04C0>}
>>> from pprint import pprint
>>> pprint(foo.__globals__)
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'bar': <function bar at 0x0000023674CC7040>,
 'foo': <function foo at 0x0000023674CF04C0>,
 'pprint': <function pprint at 0x0000023674CF0670>}
>>> foo.__init__
<method-wrapper '__init__' of function object at 0x0000023674CF04C0>
>>> foo.__hash__
<method-wrapper '__hash__' of function object at 0x0000023674CF04C0>
>>> foo.__kwdefaults__
>>> foo.__name__
'foo'
>>> foo.__qualname__
'foo'
>>> foo.__sizeof__
<built-in method __sizeof__ of function object at 0x0000023674CF04C0>
>>> foo.__str__
<method-wrapper '__str__' of function object at 0x0000023674CF04C0>
>>> foo.__repr__
<method-wrapper '__repr__' of function object at 0x0000023674CF04C0>
>>> foo.__init_subclass__
<built-in method __init_subclass__ of type object at 0x00007FFD4E9F37F0>
>>> 
>>> 
>>> 
>>> foo
<function foo at 0x0000023674CF04C0>
>>> bar
<function bar at 0x0000023674CC7040>
>>> import inspect
>>> pprint(inspect.getsource(foo))
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    pprint(inspect.getsource(foo))
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 985, in getsource
    lines, lnum = getsourcelines(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 967, in getsourcelines
    lines, lnum = findsource(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 798, in findsource
    raise OSError('could not get source code')
OSError: could not get source code
>>> inspect.getsource(bar)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    inspect.getsource(bar)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 985, in getsource
    lines, lnum = getsourcelines(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 967, in getsourcelines
    lines, lnum = findsource(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 798, in findsource
    raise OSError('could not get source code')
OSError: could not get source code
>>> 

>>> lines = inspect.getsource(bar)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    lines = inspect.getsource(bar)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 985, in getsource
    lines, lnum = getsourcelines(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 967, in getsourcelines
    lines, lnum = findsource(object)
  File "C:\Users\17033\AppData\Local\Programs\Python\Python38\lib\inspect.py", line 798, in findsource
    raise OSError('could not get source code')
OSError: could not get source code
>>> 
= RESTART: G:/Python Coding/DeclaringDecorators/testing getting object source code for functions__from IDLE shell.py
>>> 
= RESTART: G:/Python Coding/DeclaringDecorators/testing getting object source code for functions__from IDLE shell.py
('def foo(*args):\n'
 '    for i,arg in enumerate(args):\n'
 '        print(f"{i}, {arg}")\n')
>>> print(lines)
def foo(*args):
    for i,arg in enumerate(args):
        print(f"{i}, {arg}")

>>> lines
'def foo(*args):\n    for i,arg in enumerate(args):\n        print(f"{i}, {arg}")\n'
>>> foo(1,2,3)
0, 1
1, 2
2, 3
>>> foo('a', (), 1,4,2)
0, a
1, ()
2, 1
3, 4
4, 2
>>> 