"""
    Wraps a function and embeds a layer of toggling
"""
from functools import wraps


def toggleDecorator(func, toggle_key: bool):
    @wraps(func)
    def wrapped(*args, **kwargs):
        if toggle_key:
            """if true, then enable/allow the extra content"""
            print('beginning of execution')
            result = func(*args, **kwargs)
            print('done with running')
            return result
        else:
            result = func(*args, **kwargs)
            return result
    return wrapped

def makeFile(file: str):
    return file + ".txt"


makeFile = toggleDecorator(makeFile, False)

print(makeFile("gis--data"))
