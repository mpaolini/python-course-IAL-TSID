'''
TEACHER comment
Build a function that given a string, returns all places that contain the string:
>>> places = find_places('IAL')
>>> places[0]
('IAL ROMA E LAZIO', 41.954964, 12.523495)


HOMEWORK: Build a function that given a place, returns a list of places nearby

Hint: use nearby search API https://developers.google.com/places/documentation/search#PlaceSearchRequests

Hint2: use requests instead of urllib, http://docs.python-requests.org/en/latest/

>>> nearby_places(41.954964, 12.523495)
[('IAL ROMA E LAZIO', 41.954964, 12.523495)]
'''

import urllib.request
import urllib.parse
import json


def find_places(place_name):
    KEY = 'AIzaSyBnTJ0P-nXBgUEut5z_EZYQVwudWl4lP1E'
    qs = urllib.parse.urlencode(
        {'query': place_name,
         'key': KEY,
         'sensor': 'false'})
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?' + qs
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode())
    return data


def nearby_place(lat, lng):
    # Hey, this is a teacher's comment
    pass
