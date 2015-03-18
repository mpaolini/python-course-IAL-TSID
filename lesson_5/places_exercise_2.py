'''
1. Website for places

Build a function that given a string, returns all websites found

Factor out all common code for place search and place details.

>>> websites = find_place_websites('IAL')
>>> websites[0] in ('http://www.ial.lazio.it/', 'http://www.ialweb.it/')
True




2. reviews for places

Find average rating for all place reviews. None if no reviews found.

(use common utilities functions written for point 1.)

>>> find_place_reviews('Pizza') is not None
True

3. modify the above functions to visit *all* the pages in the search result
'''

import requests


KEY = 'AIzaSyDv4yY43goypjC6BXZYCcaaXySvbsFAxTA'

url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
url_details = 'https://maps.googleapis.com/maps/api/place/details/json'


def find_place_websites(place_name):
    params = {'query': place_name,
              'key': KEY}
    resp = requests.get(url, params=params)
    data = resp.json()
    websites = []
    for place in data['results']:
        resp2 = requests.get(
            url_details,
            params={'placeid': place['place_id'],
                    'key': KEY}
        )
        data2 = resp2.json()
        websites.append(data2['result']['website'])
    return websites


def find_place_reviews(place_name):
    params = {'query': place_name,
              'key': KEY}
    resp = requests.get(url, params=params)
    data = resp.json()
    ratings = []
    for place in data['results']:
        resp2 = requests.get(
            url_details,
            params={'placeid': place['place_id'],
                    'key': KEY}
        )
        data2 = resp2.json()
        if 'rating' in data2['result']:
            ratings.append(data2['result']['rating'])
    if len(ratings) == 0:
        return None
    return sum(ratings) / len(ratings)
