# Run twitter example with circus process manager

1. install circus (even outside the virtualenv)

    sudo pip3 install circus

2. make sure this `circus.ini` file is present
3. set the `TWITTER_APP_ID` and `TWITTER_APP_SECRETS` env vars

    export TWITTER_APP_ID=XXX
    export TWITTER_APP_SECRET=XXX

4. create a virtualenv and install twitter_example on it

    virtualenv -p python3 virtual
    source virtual/bin/activate
    pip install <package_url.tar.gz>

5. run circus with:

    circusd circus.ini
