# python standard library
import base64
import requests
import psycopg2

import logging

import logentries
logger = logging.getLogger('my_program')
logger.addHandler(
    logentries.LogentriesHandler('xxxxx')
)
logger.setLevel(logging.INFO)


def get_token(client_id, client_secret):
    credentials = '{}:{}'.format(client_id, client_secret)
    credentials_b64 = base64.b64encode(credentials.encode())
    resp = requests.post(
        'https://api.twitter.com/oauth2/token',
        headers={
            'Authorization': 'Basic {}'.format(credentials_b64.decode())
        },
        data={'grant_type': 'client_credentials'}
    )
    if resp.status_code == 200:
        data = resp.json()
        return data['access_token']
    else:
        raise ValueError(
            'error in request, code={} body={}'.format(
                resp.status_code, resp.text
            )
        )


def search_tweets(what, token):
    '''
    Returns:
      a list of tweets (dictionaries)
    '''
    url = 'https://api.twitter.com/1.1/search/tweets.json'
    resp = requests.get(
        url,
        headers={'Authorization': 'Bearer {}'.format(token)},
        params={'q': what, 'lang': 'it'}
    )
    resp.raise_for_status()
    data = resp.json()
    return data['statuses']


def save_tweets(tweets):
    conn = psycopg2.connect(host='localhost',
                            port=5432,
                            dbname='lesson_10',
                            user='test_10',
                            password='test_10')
    curs = conn.cursor()
    for tweet in tweets:
        curs.execute(
            'INSERT INTO tweets2 (id, date, text) VALUES (%s, %s, %s)',
            (tweet['id'], tweet['created_at'], tweet['text'])
        )
    conn.commit()
    conn.close()


if __name__ == '__main__':
    import os
    import sys
    logger.info('getting token...')
    if 'TWITTER_APP_ID' not in os.environ:
        logger.error('config error')
    token = get_token(
        os.environ['TWITTER_APP_ID'],
        os.environ['TWITTER_APP_SECRET']
    )
    print('getting tweets...')
    tweets = search_tweets(sys.argv[1], token)
    print('saving tweets...')
    save_tweets(tweets)
    print('OK!')
