.PHONY: help requirements requirements_test destroy_db init_db lint test run

VENV_BASE ?= quotes-simple-web
VENV_ACTIVATE := $(VENV_BASE)/bin/activate
PYTHON := ${VENV_BASE}/bin/python3

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

venv:	## create virtualenv
	@if [ ! -d "$(VENV_BASE)" ]; then \
		virtualenv -p python3 $(VENV_BASE); \
	fi

requirements:	## install requirements
requirements: venv
	@echo Install requirements
	@${PYTHON} -m pip install -r requirements.txt > /dev/null

requirements_test:	## install test requirements
requirements_test: requirements
	@echo Install test requirements
	@${PYTHON} -m pip install -r requirements_test.txt > /dev/null

destroy_db:	## destroy docker database
	@echo Destroy mongo
	@docker rm -f mongo > /dev/null || echo Not mongo running

init_db:	## create docker database
init_db: destroy_db
	@echo Starting mongo
	@docker run -d --name mongo -e MONGO_INITDB_ROOT_USERNAME=test \
	-e MONGO_INITDB_ROOT_PASSWORD=test1234 -p 27017:27017 mongo > /dev/null

lint:	## run pycodestyle
lint: requirements_test
	@echo Running linter
	@${PYTHON} -m pycodestyle .

test:	## run tests and show report
test: lint init_db
	@echo Running tests
	@${PYTHON} -m coverage run -m unittest discover
	@${PYTHON} -m coverage report -m

run:	## run project
run: requirements
	${PYTHON} -m quotes
