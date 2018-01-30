========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |landscape| |scrutinizer| |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/django-auth0-user/badge/?style=flat
    :target: https://readthedocs.org/projects/django-auth0-user
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/django-auth0-user.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/django-auth0-user

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/django-auth0-user?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/django-auth0-user

.. |requires| image:: https://requires.io/github/techdragon/django-auth0-user/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/django-auth0-user/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/techdragon/django-auth0-user/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/django-auth0-user

.. |landscape| image:: https://landscape.io/github/techdragon/django-auth0-user/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/django-auth0-user/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/django-auth0-user/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/django-auth0-user
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/django-auth0-user.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-auth0-user

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/django-auth0-user/v0.12.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/django-auth0-user/compare/v0.12.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-auth0-user.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-auth0-user

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-auth0-user.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-auth0-user

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-auth0-user.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-auth0-user

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/techdragon/django-auth0-user/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/techdragon/django-auth0-user/


.. end-badges

Django Authentication and Authorisation using Auth0 and Python Social Auth

Warning, this library is under active development, it is also not 1.0 yet, and has a sort of 'production' user already. Documentation, bugs, features, and pretty much everything is in flux.


* Free software: BSD license

Installation
============

::

    pip install django-auth0-user

Documentation
=============

https://django-auth0-user.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
