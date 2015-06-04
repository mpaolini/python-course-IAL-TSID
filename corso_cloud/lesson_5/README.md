# Final exam

Write a python program that periodically reports cpu information
and logs it to logentries.

You can use the `os.getloadavg()` function

The program has a simple build/publish
procedure and includes all the
needed documentation for the sysadmin
to run it on the server.


## Build the package

    python setup.py sdist


## Publish the archive on s3

    python publish.py

or alternatively, use a bash script and the
`aws s3` CLI:

    ./publish.sh


## Deploy it on the server

    pip install https://s3.amazonaws.com/<bucket>/<package>


## Run it on the server

    python -m cpuinfo.main <logentries token>
