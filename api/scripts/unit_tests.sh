#!/bin/bash

echo Starting mongo
docker run -d --name mongo -e MONGO_INITDB_ROOT_USERNAME=test -e MONGO_INITDB_ROOT_PASSWORD=test1234 -p 27017:27017 mongo &> /dev/null || docker start mongo &> /dev/null

echo Runing tests
python -m unittest discover

