#!/usr/bin/python3
"""task-10"""
from models import storage
from models.user import User
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'])
@app_views.route('/users/<user_id>', methods=['GET'])
def users_to_dict(user_id=None):
    """ Users to dictionary """
    lista = []
    for i in storage.all(User):
        lista.append(storage.all(User)[i].to_dict())
    if user_id is None:
        return jsonify(lista)
    else:
        for i in lista:
            if i['id'] == user_id:
                return jsonify(i)
        return abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """ Delete user """
    obj = storage.get(User, user_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/', methods=['POST'])
def post_user():
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
            return abort(404)
        else:
            for key, value in data.items():
                if key == 'first_name':
                    setattr(obj, key, value)
                elif key == 'last_name':
                    setattr(obj, key, value)
            obj.save()
            return jsonify(obj.to_dict()), 200
