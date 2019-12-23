# lynq.me

## Install requirements

```
pipenv install
```

## Run

### Development

```
python main.py
```

### Production: Gunicorn

```
gunicorn -b 0.0.0.0:<port> main:app
```

### Production: Docker

```
docker build . -t lynq.me
docker run -p 6345:6345 lynq.me
```
