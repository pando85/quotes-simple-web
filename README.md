[![Build Status](https://travis-ci.org/pando85/quotes-simple-web.svg?branch=master)](https://travis-ci.org/pando85/quotes-simple-web)

# quotes

Simple web server for serving quotes of famous people.

## Dev

Run app:

```bash
python -m quotes
```


Run mongo:

```bash
docker run -d --name mongo -e MONGO_INITDB_ROOT_USERNAME=test -e MONGO_INITDB_ROOT_PASSWORD=test1234 -p 27017:27017 mongo
```

Connect mongo cli:

```bash
docker exec -it mongo mongo --authenticationDatabase "admin" -u test -p test1234
```

## Tests

Run tests:
```bash
python -m unittest discover
```

### Production

**Warning**: aiohttp is [slower with gnunicorn](https://docs.aiohttp.org/en/stable/deployment.html#start-gunicorn). Basic `python -m quotes` execution is prefered.
