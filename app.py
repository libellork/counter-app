import os
from flask import Flask
import redis

app = Flask(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))
cache = redis.Redis(host=redis_host, port=redis_port)

@app.route('/')
def hello():
    count = cache.incr('hits')
    return f'이 페이지는 {count}번 조회되었습니다! (host: {redis_host})\n'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)