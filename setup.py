import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'betsy',
    version = '0.0.1-dev',
    author = 'Guy Jacks',
    author_email = 'guy.jacks@gmail.com',
    description = 'Betsy makes JSON easy as Py!',
    long_description = read('README')
)
