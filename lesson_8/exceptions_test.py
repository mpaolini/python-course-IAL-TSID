# exceptions_test.py


def all_ints():
    n = 1
    while True:
        step = yield n
        if step is None:
            step = 1
        if step <= 0:
            raise ValueError('step must be a positive int')
        n += step


def not_useful_at_all():
    return 1
