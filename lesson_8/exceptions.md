# exceptions exercise

Write a generator function that yields all ints stepping by 1 (default)
or using the step value sent into the generator.

    >>> import exceptions_test
    >>> ints = exceptions_test.all_ints()
    >>> next(ints)
    1
    >>> next(ints)
    2
    >>> ints.send(3)
    5
    >>> ints.send(-1)
    Traceback (most recent call last):
        ...
    ValueError: step must be a positive int
