from typing import Tuple, Any


class AbstractDecorator:
    """
        Any decorator wraps a function but their are common cases and
        consistent features/data and information that all decorators share.
    """
    decoratorArgs: Tuple[Any, ...]

    def __init__(self, someFunc=None, someName="", *args, **kwargs):
        self.decoratorName = someName
        self._func = someFunc

    @property
    def func(self):
        return self._func

    @func.setter
    def func(self, someFunc):
        if someFunc is not None:
            self._func = someFunc
        else:
            raise ValueError("Given function not valid or does not exist")

    @classmethod
    def fromName(cls, someName: str):
        """
            Constructor from decorator name
            @rtype: new instance of class using name value
        """
        cls.decoratorName = someName
        return cls(None, someName, "", "")

    def decoratorInfo(self):
        """
            Pretty print decorator data
        """
        header = f"Decorator '{self.decoratorName}'" + f"\n-----------" + len(self.decoratorName) * "-"
        data = f"wrapped func: {self.func}"
        return header + "\n" + data

    def __repr__(self):
        return self.decoratorInfo()

    def __str__(self):
        return f"<AbstractDecorator> &name{self.decoratorName} &func{self.func}"
