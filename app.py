from flask import Flask, g

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)

@app.before_request
def before_request():
    """Connect to the db before any request"""
    if not hasattr(g, 'db'):
        g.db = models.DATABASE
        g.db.connect()

@app.after_request
def after_request(response):
    """Close the connection to the DB"""
    g.db.close()
    return response


if __name__ == '__main':
    app.run(debug=DEBUG, host=HOST, port=PORT)
