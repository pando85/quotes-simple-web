# quotes-simple-web [![Build Status](https://travis-ci.org/pando85/quotes-simple-web.svg?branch=master)](https://travis-ci.org/pando85/quotes-simple-web) [![Docker:build](https://img.shields.io/docker/build/pando85/quotes-simple-web.svg)](https://hub.docker.com/r/pando85/quotes-simple-web/) [![License: GPL v3+](https://img.shields.io/badge/License-GPL%20v3%2B-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[![Code Climate](https://codeclimate.com/github/pando85/quotes-simple-web/badges/gpa.svg)](https://codeclimate.com/github/pando85/quotes-simple-web)  [![LGTM JS](https://img.shields.io/lgtm/grade/javascript/g/pando85/quotes-simple-web.svg?logo=lgtm)](https://lgtm.com/projects/g/pando85/quotes-simple-web/context:javascript)

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
