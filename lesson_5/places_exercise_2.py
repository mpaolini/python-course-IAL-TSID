'''
1. Website for places

Build a function that given a string, returns all websites found

Factor out all common code for place search and place details.

>>> websites = find_place_websites('IAL')
>>> websites[0]
'http://www.ial.lazio.it/'


2. reviews for places

Find average rating for all place reviews. None if no reviews found.

(use common utilities functions written for point 1.)

>>> find_place_reviews('IAL')
3.75

3. modify the above functions to visit *all* the pages in the search result
'''

import urllib.request
import urllib.parse
import json

KEY = 'AIzaSyBnTJ0P-nXBgUEut5z_EZYQVwudWl4lP1E'


def find_place_websites(place_name):
    return []


def find_place_reviews(place_name):
    return 0.0
