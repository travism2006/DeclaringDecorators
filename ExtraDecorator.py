class ExtraDecorator:
    """
        Any decorator wraps a function but their are common cases and
        consistent features/data and information that all decorators share.
    """

    def __init__(self, decName: str = "", funcName: str = ""):
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

    # find the binary value/representation of 2 decorator names (since python doesn't actually have/use real pointers)
    # then  then find their hamming distance


class CompDec:
    """
        Compare decorators in new ways.
    """

    @classmethod
    def hamDistCall(cls, dec1Name: str, dec2Name: str):
        if dec1Name == "":
            raise ValueError("Name of decorator 1 is invalid.")
        elif dec1Name is not str or dec1Name is None:
            raise TypeError("Invalid type provided for decorator 1.")
        elif dec1Name.startswith("0b") or dec1Name.startswith("0x") or dec1Name.startswith("0o"):
            raise ValueError("Str value provided is not a valid name for a decorator object.")

        if dec2Name == "":
            raise ValueError("Name of decorator 2 is invalid.")
        elif dec2Name is not str or dec2Name is None:
            raise TypeError("Invalid type provided for decorator 2.")
        elif dec2Name.startswith("0b") or dec2Name.startswith("0x") or dec2Name.startswith("0o"):
            raise ValueError("Str value provided is not a valid name for a decorator object.")

    # Compare using hamming distance of 2 decorators if the bin() str values are equal length
    @classmethod
    def hamDist_PureCharComp(cls, s1: str, s2: str):
        """
            Assumes strings of equal length. Calculates the Hamming Distance based on pure char to char comparison.
        """
        distance = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                distance += 1
        return distance

    @classmethod
    def hamDist_BinaryComp(cls, dec1Name: str, dec2Name: str):
        """
            Assumes equal length names for the decorators. Calls bin() and find the hamming distance similar to
            hamDist_PureCharComp
        """
        distance = 0
        binDec1 = bin(hash(dec1Name))
        binDec2 = bin(hash(dec2Name))
        binDec1 = binDec1[binDec1.index('b') + 1:]
        binDec2 = binDec2[binDec2.index('b') + 1:]
        for i in zip(binDec1, binDec2):
            if i[0] != i[1]:
                print(i)
                distance += 1
        return distance

    # def binaryDiffByName(cls, decObj1: str, decObj2: str):
    #     if len(bin(hash(decObj1))) == len(bin(hash(decObj2))):
    #         # if len is same then find hamming distance from just their names alone
    #         a
    #     pass
