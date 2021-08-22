class ExtraDecorator:
    """
        Any decorator wraps a function but their are common cases and
        consistent features/data and information that all decorators share.
    """

    def __init__(self, decName: str = "", funcName: str = "") -> object:
        """
            Optional args: decName, funcName

        """
        self.decoratorName = decName
        self.func = funcName

    @classmethod
    def fromName(cls, someName: str):
        """
            Constructor from desired decorator name
        """
        cls.decoratorName = someName
        return cls(decName=someName)

    @classmethod
    def fromFunctionName(cls, someFunctionName: str) -> object:
        cls.func = someFunctionName
        return cls(funcName=someFunctionName)

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
        return f"<AbstractDecorator> &name {self.decoratorName} &func {self.func}"

    # TODO make iterable aspect
    # nested TODO add 2 methods for iterating
    # TODO make __next__() method
    # TODO make __iter__() method
    # TODO make comparisons between any 2 decorators

    # Compare using hamming distance of 2 decorators
    # find the binary value/representation of 2 decorator names (since python doesn't actually have/use real pointers)
    # then if the bin() str values are equal length then find their hamming distance
