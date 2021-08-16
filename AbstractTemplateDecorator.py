class AbstractBoilerplateDecorator:
    """
        Boilerplate inheritable decorators for common use cases
    """

    @staticmethod
    def log2File(self) -> str:
        # Child implements logic to log to generic file
        pass

    @staticmethod
    def lenTimeinMS(self):
        # Child implements basic function time calculation
        pass



# TODO [idea] make class for "with" statement support (e.g. "with ___ as targetVar:")

# TODO [idea] make html and css (engine?) support/feature to generate file.html with styles for showing all decorators
