#!/usr/bin/python3
"""task-0"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def c_storage():
    """close the storage"""
    storage.close()


@app.route('/', strict_slashes=False)
def h_hbnb():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
