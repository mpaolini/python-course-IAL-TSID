# Package exercise

Write a `my_utils` package that contains two modules: `math` and `strings`.

Implement a `add_ints` function in `my_utils.math`:

    >>> import my_utils.math
    >>> my_utils.math.add_ints(1, 2)
    3
    >>> my_utils.math.add_ints(1, 'ciao')
    Traceback (most recent call last):
        ...
    TypeError: ints required


Implement a `add_strings` function in `my_utils.strings`:

    >>> import my_utils.strings
    >>> my_utils.strings.add_strings('bob', 'cat')
    'bobcat'
    >>> my_utils.strings.add_strings('bob', 1)
    Traceback (most recent call last):
        ...
    TypeError: strings required
