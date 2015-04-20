'''
Example of twitter API usage.

Requires Twitter APP credentials stored in the following env vars:
  APP_KEY
  APP_SECRET

Saves tweets in the DB.
'''

import base64
import requests
import psycopg2


def get_bearer_token(consumer_key, app_secret):
    credentials = '{}:{}'.format(consumer_key, app_secret)
    credentials_enc = base64.b64encode(credentials.encode())
    resp = requests.post(
        'https://api.twitter.com/oauth2/token',
        headers={'Authorization': 'Basic {}'.format(credentials_enc.decode())},
        data={'grant_type': 'client_credentials'}
    )
    resp.raise_for_status()
    resp_data = resp.json()
    return resp_data['access_token']


def get_tweets(word, token):
    '''
    Returns:
      a list of tweets (dictionaries) as returned by twitter API
    '''
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    resp = requests.get(
        url,
        params={'q': word, 'lang': 'it'},
        headers={'Authorization': 'Bearer {}'.format(token)}
    )
    resp.raise_for_status()
    data = resp.json()
    return data['statuses']


def save_tweets(tweets):
    '''

    To create the table do:
        curs.execute('CREATE TABLE tweets (
            text varchar(500),
            date varchar(600),
            id varchar(600))'
        )
    '''
    conn = psycopg2.connect(user='test_10', password='test_10',
                            dbname='lesson_10', host='localhost',
                            port=5432)
    curs = conn.cursor()
    for tweet in tweets:
        curs.execute(
            'INSERT INTO tweets VALUES (%s, %s, %s)',
            (tweet['text'], tweet['created_at'], tweet['id_str'])
        )
    conn.commit()
    curs.close()
    conn.close()


if __name__ == '__main__':
    import os
    import sys
    print('getting bearer token')
    token = get_bearer_token(
        os.environ['APP_KEY'],
        os.environ['APP_SECRET']
    )
    print('bearer token created!')
    print('getting tweets')
    tweets = get_tweets(sys.argv[1], token)
    print('got {} tweets'.format(len(tweets)))
    save_tweets(tweets)
