.PHONY: help test run

.DEFAULT: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/\n\t/'

build:	## build images
	docker-compose build

run:	## run project
run: build
	docker-compose up -d

test:	## run end to end tests
test: run
	npm install
	./node_modules/.bin/nightwatch -e chrome,firefox
	docker-compose down
