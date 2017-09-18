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

.. |docs| image:: https://readthedocs.org/projects/django-auth0-auth/badge/?style=flat
    :target: https://readthedocs.org/projects/django-auth0-auth
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/techdragon/django-auth0-auth.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/techdragon/django-auth0-auth

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/techdragon/django-auth0-auth?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/techdragon/django-auth0-auth

.. |requires| image:: https://requires.io/github/techdragon/django-auth0-auth/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/techdragon/django-auth0-auth/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/techdragon/django-auth0-auth/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/techdragon/django-auth0-auth

.. |landscape| image:: https://landscape.io/github/techdragon/django-auth0-auth/master/landscape.svg?style=flat
    :target: https://landscape.io/github/techdragon/django-auth0-auth/master
    :alt: Code Quality Status

.. |codeclimate| image:: https://codeclimate.com/github/techdragon/django-auth0-auth/badges/gpa.svg
   :target: https://codeclimate.com/github/techdragon/django-auth0-auth
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/django-auth0-auth.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/django-auth0-auth

.. |commits-since| image:: https://img.shields.io/github/commits-since/techdragon/django-auth0-auth/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/techdragon/django-auth0-auth/compare/v0.1.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/django-auth0-auth.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/django-auth0-auth

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/django-auth0-auth.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/django-auth0-auth

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/django-auth0-auth.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/django-auth0-auth

.. |scrutinizer| image:: https://img.shields.io/scrutinizer/g/techdragon/django-auth0-auth/master.svg
    :alt: Scrutinizer Status
    :target: https://scrutinizer-ci.com/g/techdragon/django-auth0-auth/


.. end-badges

Django Authentication and Authorisation using Auth0 and Python Social Auth

* Free software: BSD license

Installation
============

::

    pip install django-auth0-auth

Documentation
=============

https://django-auth0-auth.readthedocs.io/

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
