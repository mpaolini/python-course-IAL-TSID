'''
MARCO

Web requests and dictionaries


1. Get all emails

>>> sorted(get_all_emails('http://private-bb81a-ialpython.apiary-mock.com/people'))
['luigi@gmail.com', 'mario@example.com', 'test2@example.com', 'test3@example.com', 'test@example.com']

2. Get people names

>>> names = get_people_names('http://private-bb81a-ialpython.apiary-mock.com/people')
>>> names['Mario Rossi']
['mario@example.com']
>>> names['Luigi Bianchi']
['luigi@gmail.com']
>>> sorted(names['Test User'])
['test2@example.com', 'test3@example.com', 'test@example.com']

3. Refactor common code for request handling
'''

import urllib.request
import json


def get_all_emails(url):
    resp = urllib.request.urlopen(url)
    data = resp.read().decode()
    return [key for key, val in json.loads(data).items()]


def get_people_names(url):
    resp = urllib.request.urlopen(url)
    data = json.loads(resp.read().decode())
    names = {}
    for email, name in data.items():
        if name in names:
            names[name].append(email)
        else:
            names[name] = [email]
    return names
