import json
import urllib.request


def unique_names():
    url = 'http://private-bb81a-ialpython.apiary-mock.com/people'
    resp = urllib.request.urlopen(url).read()
    data = json.loads(resp.decode())

    names = set()
    for name in data.values():
        names.add(name)
    return list(names)

    names = []
    for name in data.values():
        if name not in names:
            names.append(name)
    return names

    return list(set(data.values()))
