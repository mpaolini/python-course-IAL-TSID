## test_1.py

Please implement a function that returns the last item of a list. If
the list is empty, return `None`

    >>> import test_1
    >>> l = [1, 3, 5]
    >>> test_1.get_last(l)
    5
    >>> test_1.get_last([]) == None
    True


## test_2.py

    >>> import test_2

Write a function get_shortest_len() that takes a list of words and returns the
length of the shortedst one one. If the list is emtpy, return `0`.

    >>> test_2.get_shortest_len(['cat', 'dog', 'penguin'])
    3

    >>> test_2.get_shortest_len([])
    0


## test_3.py

    >>> import test_3

Write a function that finds out all lines that begin with a given string.

It accepts two arguments: the name of the origin file and a string.

It returns a generator that yields one line at a time.

    >>> lines = test_3.grep_lines('test_3_helper.txt', 'hey')
    >>> next(lines)
    'hey Joe'
    >>> next(lines)
    'hey you'
    >>> next(lines)
    Traceback (most recent call last):
        ...
    StopIteration
    >>> lines = test_3.grep_lines('test_3_helper.txt', 'cat')
    >>> next(lines)
    'cat'
    >>> next(lines)
    'catamaran'
    >>> next(lines)
    Traceback (most recent call last):
        ...
    StopIteration


## test_4.py

    >>> import test_4

Write a function that computes the number of occurrence of each word contained
in it.

It returns a dictionary with words as keys and number of occurrences as values.


    >>> test_4.count_words('merry christmas')
    {'merry': 1, 'christmas': 1}
    >>> test_4.count_words('white cat and black cat')
    {'cat': 2, 'white': 1, 'black': 1, 'and': 1}


## test_5.py


    >>> import test_5

Write a function that sorts integers passed in as list and returns a string
where the sorted ints are separated by a comma (`,`)

    >>> test_5.sort_ints_csv([2, 5, 1, 4])
    '1, 2, 4, 5'
    >>> test_5.sort_ints_csv([100, 4, 2])
    '2, 4, 100'


## test_6.py

Write a function that concatenates strings. Strings can be passed as variable
number of args.

    >>> import test_6
    >>> test_6.concatenate_strings('a', 'b')
    'ab'
    >>> test_6.concatenate_strings('a', 'b', 'c')
    'abc'


## test_7.py

The remote endpoint http://private-bb81a-ialpython.apiary-mock.com/workstations
keeps the status of all workstation in the laboratory.

Implement python client that queries the remote resource and returns all the
ip addresses of the workstations that are in `down` status.

Output sorting is not relevant.

    >>> import test_7
    >>> ips = test_7.get_broken_ips()
    >>> sorted(ips)
    ['192.168.0.5', '192.168.0.8']
