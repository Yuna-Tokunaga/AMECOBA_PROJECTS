# server.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello python flask world!!"

if __name__ == "__name__":
    app.run()