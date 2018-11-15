# quotes-simple-web [![Build Status](https://travis-ci.org/pando85/quotes-simple-web.svg?branch=master)](https://travis-ci.org/pando85/quotes-simple-web) [![License: GPL v3+](https://img.shields.io/badge/License-GPL%20v3%2B-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![analytics](https://www.google-analytics.com/collect?v=1&t=pageview&_s=1&ds=github&dr=https%3A%2F%2Fgithub.com%2Fnetdata%2Fnetdata&dl=https%3A%2F%2Fmy-netdata.io%2Fgithub%2Freadme&_u=MAC~&cid=5792dfd7-8dc4-476b-af31-da2fdb9f93d2&tid=UA-64295674-3)]()

[![Code Climate](https://codeclimate.com/github/pando85/quotes-simple-web/badges/gpa.svg)](https://codeclimate.com/github/pando85/quotes-simple-web)  [![LGTM JS](https://img.shields.io/lgtm/grade/javascript/g/pando85/quotes-simple-web.svg?logo=lgtm)](https://lgtm.com/projects/g/pando85/quotes-simple-web/context:javascript) [![LGTM PYTHON](https://img.shields.io/lgtm/grade/python/g/pando85/quotes-simple-web.svg?logo=lgtm)](https://lgtm.com/projects/g/pando85/quotes-simple-web/context:python)

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
