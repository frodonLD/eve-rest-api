#!/usr/bin/env python
"""
setup.py
based on https://github.com/pyeve/eve/blob/master/setup.py and
https://docs.python.org/3.6/distutils/setupscript.html
"""
from setuptools import setup, find_packages

DESCRIPTION = ("SMS REST API Based on Eve")
with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

install_requires = [
    'eve',
],
setup_requires=[
    'pytest-runner',
],
tests_require=[
    'pytest',
],

setup(
    name='sms-api',
    version='0.0.1',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Frejus Gbaguidi',
    author_email='fh.gbaguidi@gmail.com',
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Development Status :: 1.0',
        'Environment :: Web Environment',
        'Intended Audience :: Private',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
