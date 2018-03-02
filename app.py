from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    redis.incr('seens')
    return 'Hello World. seen %s times.' % redis.get('seens')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
