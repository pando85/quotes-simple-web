[![Build Status](https://travis-ci.org/pando85/quotes-simple-web.svg?branch=master)](https://travis-ci.org/pando85/quotes-simple-web)

# quotes-simple-web

Simple web server for serving quotes.


## Deployment

Write your quotes in `./api/data/quotes.json` with [this format](https://github.com/pando85/quotes-simple-web/blob/master/api/test/data/quotes.json).


### Requirements:

- docker
- docker-compose

### Run

```bash
make run
```

### Tests

End to end tests:

```
make test
```
