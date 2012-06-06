from __future__ import division, absolute_import, unicode_literals, print_function

from setuptools import setup

def read_requirements(path='requirements.txt'):
    # There has /got/ to be a better way to do this.
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    before_comment = lambda line: line.split('#', 1)[0].strip()
    return list(filter(None, map(before_comment, lines)))

setup(
    name='{{module.name}}',
    version='{{module.version}}',
    description='{{module.description}}',
    author='{{author.name}}',
    author_email='{{author.email}}',
    url='{{module.url}}',
    packages=['{{module.name}}'],
    install_requires=read_requirements(),
    )
