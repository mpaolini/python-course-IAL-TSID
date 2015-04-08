# strings.py


def add_strings(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError('strings required')
    return a + b
