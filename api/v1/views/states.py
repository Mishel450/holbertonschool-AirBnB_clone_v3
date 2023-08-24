#!/usr/bin/python3
"""task-0"""
from models import storage
from models.state import State
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/states/', methods=['GET'])
@app_views.route('/states/<state_id>', methods=['GET'])
def states_to_dic(state_id=None):
    """states in to_dict format"""
    lista = []
    for i in storage.all(State):
        lista.append(storage.all(State)[i].to_dict())
    if state_id is None:
        return jsonify(lista)
    else:
        for i in lista:
            if i['id'] == state_id:
                return jsonify(i)
        return abort(404)


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """it deletes from objects"""
    i = "State" + "." + state_id
    the_dict = storage.all(State).keys()
    if i in the_dict:
        del storage[i]
        storage.save()
        return jsonify({}), 200
    else:
        return abort(404)


@app_views.route('/states/', methods=['POST'])
def post_state():
    """search and create a state"""
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    elif 'name' not in data:
        error_m = ' Missing name'
        return jsonify(error_m), 400
    else:
        obj = State()
        obj.name = data['name']
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def put_state(state_id):
    """puts the diccionary in the test"""
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    else:
        obj = storage.get(State, state_id)
        if obj is None:
            return abort(404)
        else:
            obj.name = data['name']
            obj.save()
            return jsonify(obj.to_dict()), 200
