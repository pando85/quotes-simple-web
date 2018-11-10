# quotes

Simple API for serving quotes.

## Dev

Run app:

```bash
make run
```

Connect mongo cli:

```bash
docker exec -it mongo mongo --authenticationDatabase "admin" -u test -p test1234
```

## Tests

Run tests:
```bash
make test
```

## Load tests

Run app:
```bash
make run
```

In another terminal:
```bash
make load_test
```

### Production

**Warning**: aiohttp is [slower with gnunicorn](https://docs.aiohttp.org/en/stable/deployment.html#start-gunicorn). Basic `python -m quotes` execution is prefered.
