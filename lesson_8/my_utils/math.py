# math.py


def add_ints(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('ints required')
    return a + b
