
# Program to help devs save time making their own decorators
# Typically in Python decorators may be used to wrap and apply to any functions
from ExtraDecorator import ExtraDecorator

# d = ExtraDecorator()
# print(d.decoratorInfo())

d2 = ExtraDecorator.fromName("MyDecorator")
# print(d2)
print(d2)

# d2.func = "bob"
print(repr(d2))
