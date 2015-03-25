## test_1.py

Please implement a function that returns the second item of a list.

    >>> import test_1
    >>> l = [1, 3, 5]
    >>> test_1.get_second(l)
    3


## test_2.py

    >>> import test_2

Write a function find_longest_word() that takes a list of words and returns the
length of the longest one.

    >>> test_2.find_longest_word(['cat', 'dog', 'penguin'])
    7

Write a function filter_long_words() that takes a list of words and an integer
n and returns the list of words that are longer than n.

    >>> test_2.filter_long_words(['cat', 'dog', 'penguin'], 5)
    ['penguin']
    >>> test_2.filter_long_words(['cat', 'dog', 'penguin'], 10)
    []


## test_3.py

    >>> import test_3

Write a function that accepts two arguments: the name of the origin file and
the name of the destination file.

The function creates (or overwrites) the destination file in which all
the lines from the original file are numbered from 1 to n
(where n is the number of lines in the file).

    >>> test_3.add_line_number('test_3_file.txt', 'test_3_file_with_lines.txt')
    >>> f = open('test_3_file_with_lines.txt', 'r')
    >>> lines = f.readlines()
    >>> lines[0]
    '1 This is a the first line\n'
    >>> lines[1]
    '2 and this is the second\n'


## test_4.py

    >>> import test_4

Represent a small bilingual lexicon as a Python dictionary in the following fashion `{"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}` and use it to translate your Christmas cards from English into Swedish. Write a function translate() that translates an english sentence in swedish

    >>> test_4.translate('merry christmas')
    'god jul'


## test_5.py


    >>> import test_5

Give the yourself a nickname. Write a function that given firs, last and nickname
returns a string made by your first name, then your nickname in parenthesis,
and then your last name.

    >>> test_5.print_name(first_name='George', last_name='Washington', nickname='Woody')
    'George (Woody) Washington'


## test_6.py

Write a function that sums numbers. Numbers can be passed as variable number
of args.

    >>> import test_6
    >>> test_6.add_ints(1, 2)
    3
    >>> test_6.add_ints(1, 2, 3)
    6


## test_7.py

Implement python client that downloads the resources from the http://private-bb81a-ialpython.apiary-mock.com/people endpoint and returns a list of *unique* names.

    >>> import test_7
    >>> names = test_7.unique_names()
    >>> sorted(names)
    ['Luigi Bianchi', 'Mario Rossi', 'Test User']
