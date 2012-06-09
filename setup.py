from __future__ import division, absolute_import, unicode_literals, print_function

from setuptools import setup

def read_requirements(path='requirements.txt'):
    # There has /got/ to be a better way to do this.
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    before_comment = lambda line: line.split('#', 1)[0].strip()
    return list(filter(None, map(before_comment, lines)))

setup(
    name='pytrigger',
    version='0.0.1',
    description='',
    author='Kevin Kelley',
    author_email='kelleyk@kelleyk.net',
    url='https://github.com/kelleyk/pytrigger',
    packages=['pytrigger'],
    install_requires=read_requirements(),
    )
