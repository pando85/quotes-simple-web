.PHONY: help requirements requirements_test destroy_db init_db lint test run load_test

VENV_BASE ?= .venv/quotes-simple-web
VENV_ACTIVATE := $(VENV_BASE)/bin/activate
PYTHON := ${VENV_BASE}/bin/python3

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

venv:	## create virtualenv
	@if [ ! -d "$(VENV_BASE)" ]; then \
		python3 -m venv $(VENV_BASE); \
	fi

requirements:	## install requirements
requirements: venv
	@echo Install requirements
	@${PYTHON} -m pip install -r requirements.txt > /dev/null

requirements_test:	## install test requirements
requirements_test: requirements
	@echo Install test requirements
	@${PYTHON} -m pip install -r requirements_test.txt > /dev/null

lint:	## run pycodestyle
lint: requirements_test
	@echo Running linter
	@${PYTHON} -m pycodestyle quotes test
	@${PYTHON} -m flake8 quotes test
	@${PYTHON} -m mypy --ignore-missing-imports quotes test

test:	## run tests and show report
test: lint
	@echo Running tests
	@${PYTHON} -m coverage run -m unittest discover
	@${PYTHON} -m coverage report -m

load_test:	## run load tests
load_test: requirements_test
	${VENV_BASE}/bin/locust --host=http://localhost:8080 -c 2500 -r 100 -t 30s --no-web

run:	## run project
run: requirements
	${PYTHON} -m quotes
