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
	until curl -k http://localhost:8080/ping ; do date; sleep 1; echo ""; ip a; ss -nlpt; docker-compose logs --no-color; docker-compose ps; docker-compose ps; docker ps -a; done
	npm install
	./node_modules/.bin/nightwatch -e chrome,firefox
	docker-compose down
