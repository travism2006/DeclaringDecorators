class AbstractDecorator:
    """
        Any decorator wraps a function but their are common cases and
        consistent features/data and information that all decorators share.
    """
    def __init__(self):
        self.decName = ""
        self.decArgs = ""
        self.decKwargs = ""
