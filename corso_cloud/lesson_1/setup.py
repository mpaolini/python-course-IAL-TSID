from setuptools import setup, find_packages

setup(
    name='twitter_example',
    version='0.1',
    description='Example of twitter API client',
    author='me',
    install_requires=['requests', 'psycopg2'],
    packages=find_packages(),
)
