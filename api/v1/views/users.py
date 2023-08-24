#!/usr/bin/python3
"""task-10"""
from models import storage
from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'])
def users_to_dict():
    """ Users to dictionary """
    list = []
    for i in storage.all(User):
        list.append(storage.all(User)[i].to_dict())
    if obj is None:
        return jsonify(list)
    else:
        for i in list:
            if i['id'] == obj:
                return jsonify(i)
        return abort(404)

@app_views.route('/users/<user_id>', methods=['POST'])
def post_user(user_id):
    """ Post user """
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    elif 'email' not in data:
        error_m = ' Missing email'
        return jsonify(error_m), 400
    elif 'password' not in data:
        error_m = ' Missing password'
        return jsonify(error_m), 400
    else:
        obj = User()
        obj.email = data['email']
        obj.password = data['password']
        obj.save()
        return jsonify(obj.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'])
def put_user(user_id):
    """ Put user """
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    else:
        obj = storage.get(User, user_id)
        if obj is None:
            abort(404)
        else:
            obj = User()
            obj.save()
            return jsonify(obj.to_dict()), 200
