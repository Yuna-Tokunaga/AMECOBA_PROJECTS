# localhost:5000/
from flask import Flask

app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Flask入門しました!'


# Flask 起動
if __name__ == "__main__": 
    app.run()