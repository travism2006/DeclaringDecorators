
# Program to help devs save time making their own decorators
# Typically in Python decorators may be used to wrap and apply to any functions

class AbstractDecorator:
    """
        Any decorator wraps a function but their are common cases and
        consistent features/data and information that all decorators share.
    """
    def __init__(self):
        self.decName = ""
        self.decArgs = ""
        self.decKwargs = ""
