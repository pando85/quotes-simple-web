#!/bin/bash
set -e

destroy_db(){
    echo Destroy mongo
    docker rm -f mongo &> /dev/null || echo Not mongo running
}

init_db(){
    destroy_db
    echo Starting mongo
    docker run -d --name mongo -e MONGO_INITDB_ROOT_USERNAME=test -e MONGO_INITDB_ROOT_PASSWORD=test1234 -p 27017:27017 mongo &> /dev/null
}

init_db

echo Runing linter
python -m pycodestyle .

echo Runing tests
coverage run -m unittest discover

echo Coverage report
coverage report -m

destroy_db
