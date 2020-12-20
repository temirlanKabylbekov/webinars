import time

import redis
from flask import Flask, request

REDIS_HOST = 'redis'
REDIS_PORT = 6379

CACHE_URL_KEY = lambda url: f'api.{url}'
CACHE_TTL = 1 * 60

PAYLOAD = 2

app = Flask(__name__)
cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)


@app.route('/not-cached/')
def not_cached():
    time.sleep(PAYLOAD)
    return 'Caching'


@app.route('/caching/')
def caching():
    cache_key = CACHE_URL_KEY(request.path)

    if cache.get(cache_key):
        return cache.get(cache_key)

    time.sleep(PAYLOAD)
    response = 'Caching'

    cache.set(cache_key, response, CACHE_TTL)

    return response
