'''
Web requests and sets


1. Is an email contained in response?

(use sets)

>>> is_email_present('test@example.com')
True
>>> is_email_present('test50@example.com')
False


2. Is name present?

(use sets)

>>> is_name_present('Luigi')
True
>>> is_name_present('Bianchi')
True
>>> is_name_present('Marta')
False

3. use requests instead of urllib
'''

import urllib.request
import json

url = 'http://private-bb81a-ialpython.apiary-mock.com/people'


def is_email_present(email):
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode())
    return email in data


def is_name_present(name):
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode())
    for first_last in data.values():
        if name in first_last:
            return True
    return False
