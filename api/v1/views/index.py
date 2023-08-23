#!/usr/bin/python3
"""task-4"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def json_return():
    return jsonify({"status": "OK"})
