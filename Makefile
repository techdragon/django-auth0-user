.PHONY: clean-pyc clean-build docs help
.DEFAULT_GOAL := help
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@perl -nle'print $& if m{^[a-zA-Z_-]+:.*?## .*$$}' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

clean: clean-build clean-pyc

clean-build: ## remove build artifacts
	rm -fr build/
#	rm -fr dist/
	rm -fr *.egg-info

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: ## check style with flake8
	flake8 django_db_auth0_user tests

test: ## run tests quickly with the default Python
	python runtests.py tests

test-all: ## run tests on every Python version with tox
	tox

coverage: ## check code coverage quickly with the default Python
	coverage run --source django_db_auth0_user runtests.py tests
	coverage report -m
	coverage html
	open htmlcov/index.html

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/django-db-auth0-user.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ django_db_auth0_user
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

release: clean ## package and upload a release
	python setup.py sdist upload
	python setup.py bdist_wheel upload

sdist: clean
	python setup.py clean --all sdist
	ls -l dist

# TODO: Tidy these up and contribute them to the upstream cookiecutter.
setup-clean:
	python setup.py clean --all

build-sdist:
	python setup.py sdist

build-bdist:
	python setup.py bdist_wheel

build: clean setup-clean build-sdist build-bdist
	ls -l dist

upload:
	twine upload --skip-existing dist/*.whl dist/*.gz
