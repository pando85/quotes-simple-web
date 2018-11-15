[![Build Status](https://travis-ci.org/pando85/quotes-simple-web.svg?branch=master)](https://travis-ci.org/pando85/quotes-simple-web)

# quotes-simple-web

Simple web server for serving quotes.


## Deployment

You will need data with this schema:
  - audio quote files in `AUDIOS_PATH`
  - json with quote files in `QUOTES_PATH`

Quote files must have [this format](https://github.com/pando85/quotes-simple-web/blob/master/api/test/data/transcripts/1.json).

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
