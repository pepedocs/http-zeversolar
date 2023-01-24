# http-zeversolar
A simple Home Assistant Sensor that reports Zevercloud Plant measurements.

# Install
1. Install python modules in a python virtual environment.

```
$ source yourpythonvirtualenv/bin/activate
$ pip install -r requirements.txt
```

# Prepare
Before running this sensor, the following environment variables need to be set.

1. API_KEY - Zevercloud API key.
2. APP_KEY - Zevercloud app key.
3. APP_SECRET - Zevercloud app secret.
4. HA_API_KEY - Home Assistant API key.
5. HA_API_URL - Home Assistant API URL in the form of "http://homeassistantipaddress:homeassistantport/api


# Run locally
```
$ cd http-zeversolar
$ python app.py
```

# Build and run docker container
```
$ cd http-zeversolar
$ docker-compose build
$ docker-compose up
```
