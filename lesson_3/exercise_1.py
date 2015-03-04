'''
Web requests and dictionaries


1. Get all emails

>>> get_all_emails('http://private-bb81a-ialpython.apiary-mock.com/people')
['mario@example.com', 'luigi@gmail.com', 'test@example.com', 'test2@example.com', 'test3@example.com']

2. Get people names

>>> get_people_names('http://private-bb81a-ialpython.apiary-mock.com/people')
{'Mario Rossi': ['mario@example.com'], 'Luigi Bianchi': ['luigi@gmail.com'], 'Test User': ['test@example.com', 'test2@example.com', 'test3@example.com']}

3. Refactor common code for request handling
'''

import urllib.request
import json


def get_all_emails(url):
    resp = urllib.request.urlopen(url)
    data = resp.read().decode()
    return json.loads(data)


def get_people_names(url):
    resp = urllib.request.urlopen(url)
    data = resp.read().decode()
    return json.loads(data)
