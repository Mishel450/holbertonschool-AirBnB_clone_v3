#!/usr/bin/python3
"""task-0"""
from models import storage
from flask import Flask, jsonify
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.errorhandler(404)
def error_handler(error):
    return jsonify({"error": "Not found"}), 404


@app.teardown_appcontext
def c_storage(excepetion):
    """close the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
