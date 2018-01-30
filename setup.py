#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='django-auth0-user',
    version='0.12.0',
    license='BSD license',
    description='Django Authentication and Authorisation using Auth0 and Python Social Auth',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Samuel Bishop',
    author_email='sam@techdragon.io',
    url='https://github.com/techdragon/django-auth0-user',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        # eg: 'aspectlib==1.1.1', 'six>=1.7',
        'social-auth-core>=1.4.0',
        'social-auth-app-django>=1.2.0',
        'django>=1.10',
        "cached-property>=1.3.0",
        'six',
    ],
    tests_require=[
        'auth0-python>=3.0.0',
        'django-environ>=0.4.3',
        'djangorestframework>=3.7.3',
        'djangorestframework-jwt>=1.11.0',
        'django-extensions>=1.7.9',
        'django-debug-toolbar>=1.8',
        'pyjwt>=1.5.3',
        'pytest>=3.0.0',
        'pytest-django>=3.1.0',
        "selenium>=3.4.3",
        "elizabeth==0.3.30",
        'retryz>=0.1.9',
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
        'drf': [
            'djangorestframework>=3.7.3',
            'djangorestframework-jwt>=1.11.0',
            'pyjwt>=1.5.3',
        ]
    },
)
