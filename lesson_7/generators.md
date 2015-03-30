# Generators exercise

Run the tests with:

    python -m doctest -v generators.md


Write your code in `generators_exercise.py` so that you can:

    >>> import generators_exercise

## Exercise 0

Implement a funciton that yields all english words

    >>> words = generators_exercise.all_english_words()
    >>> next(words)
    'A'
    >>> next(words)
    "A's"

## Exercise 1

Implement a function that yields every other item of an iterator.

    >>> names = ['Marco', 'Mario', 'Giovanni', 'Michele']
    >>> list(generators_exercise.filter_every_other(names))
    ['Marco', 'Giovanni']


Can also be used with a long sequence:

    >>> words = generators_exercise.all_english_words()
    >>> every_other_word = generators_exercise.filter_every_other(words)
    >>> next(every_other_word)
    'A'
    >>> next(every_other_word)
    "AA's"


## Exercise 2

Implement a function that yields all words longer than the argument `n`:

    >>> words = generators_exercise.all_english_words()
    >>> longer_words = generators_exercise.filter_longer(words, 4)
    >>> next(longer_words)
    "ABM's"
    >>> next(longer_words)
    "ACTH's"


## Exercise 3

Implement a function that yields 1 2 and three

    >>> one_two_3 = generators_exercise.one_two_three()
    >>> next(one_two_3)
    1
    >>> next(one_two_3)
    2
    >>> next(one_two_3)
    3
    >>> next(one_two_3)
    Traceback (most recent call last):
        ...
    StopIteration
