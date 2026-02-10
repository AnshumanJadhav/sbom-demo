from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, SBOM Demo!"

if __name__ == '__main__':
    app.run()
