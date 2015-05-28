"""
Creates an ec2 instance on AWS, downloading the ssh key.

Configuration:

    make sure you set up your aws credentials on the 'tsid-test'
    profile

Usage:

    python create_machine.py <key_name>

**NOTE** key name must be unique among all participants

"""
import glob

import botocore.session


def publish(fname):
    session = botocore.session.Session(
        session_vars={'profile': (None, None, 'tsid-test')}
    )
    s3 = session.create_client('s3')
    s3.create_bucket(Bucket='tsid_marco_test')
    with open(fname, 'rb') as f:
        s3.put_object(
            Bucket='tsid_marco_test',
            Key='archive.tar.gz',
            Body=f,
            ACL='public-read')
        print('published file available at http://s3.amazonaws.com/tsid_marco_test/archive.tar.gz')

if __name__ == '__main__':
    for fname in glob.glob('dist/twitter_example-*.tar.gz'):
        publish(fname)
