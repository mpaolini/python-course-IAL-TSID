"""Test environment variables

Write a python function that takes secrets out
of the environment variable MY_SECRET and prints
it to standard output.
"""


def print_my_secret():
    import os
    import pdb; pdb.set_trace()
    print('sono'
          ' marco')
    print('my secret '
          'is: {}'.format(os.environ['MY_SECRET']))


if __name__ == '__main__':
    print_my_secret()
