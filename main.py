
# Program to help devs save time making their own decorators
# Typically in Python decorators may be used to wrap and apply to any functions
from AbstractDecorator import AbstractDecorator

# d = AbstractDecorator()
# print(d.decoratorInfo())

d2 = AbstractDecorator.fromName("MyDecorator")
# print(d2)
print(d2)

# d2.func = "bob"
print(repr(d2))
