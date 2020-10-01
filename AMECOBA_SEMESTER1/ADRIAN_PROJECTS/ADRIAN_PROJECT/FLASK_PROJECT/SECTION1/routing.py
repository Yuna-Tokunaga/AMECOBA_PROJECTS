from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/script') # localhost:5000/script
def hello():
    return 'Hello, World'