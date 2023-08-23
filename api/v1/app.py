#!/usr/bin/python3
"""task-0"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_handler():
    return jsonify({"error": "Not found"})


@app.teardown_appcontext
def c_storage(excepetion):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
