from flask import Flask, g
from flask_login import LoginManager()

import models

DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.secret_key = 'sd123.-/sd13¡?*asd123asd46qwegdsnmdmh3487ryduiskwjh'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view('login')

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the db before any request"""
    if not hasattr(g, 'db'):
        g.db = models.DB
        g.db.connect()

@app.after_request
def after_request(response):
    """Close the connection to the DB"""
    g.db.close()
    return response


if __name__ == '__main':
    app.run(debug=DEBUG, host=HOST, port=PORT)
