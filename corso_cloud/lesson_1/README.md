# twitter client example

## What is twitter client example

- uses the twitter api to fetch tweets searching for a term
- saves tweets into postgres db


## Build

to build the package do:

    python setup.py sdist

You can find your package archive in `dist/twitter_example-XXXX.tar.gz`


## Publish

Copy archive from `dist` directory into dropbox and
share its url.

If you have your dropbox configured to sync automatically do:

    python publish.py


## Install

To install this package on your server run:

    pip install https://www.dropbox.com/s/q9kblg4qw91tseo/twitter_example-0.1.tar.gz?dl=1


## Run

To run the app on your servers do:

    python -m twitter_example XXXXX YYYYY



## Test

    ????


## Logging and monitoring

The app will log all its activity on logentries and `WARNINGS` and
`ERRORS` are delivered to a slack channel via web hook.
