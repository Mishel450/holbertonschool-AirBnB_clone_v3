#!/usr/bin/python3
"""task-0"""
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/amenities/', methods=['GET'])
@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def amenity_to_dic(amenity_id=None):
    """states in to_dict format"""
    lista = []
    for i in storage.all(Amenity):
        lista.append(storage.all(Amenity)[i].to_dict())
    if amenity_id is None:
        return jsonify(lista)
    else:
        for i in lista:
            if i['id'] == amenity_id:
                return jsonify(i)
        return abort(404)


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_state(amenity_id):
    """it deletes from objects"""
    fetched_obj = storage.get(Amenity, amenity_id)
    if fetched_obj is None:
        abort(404)
    storage.delete(fetched_obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities',
                 methods=['POST'], strict_slashes=False)
def post_city():
    """search and create a state"""
    from models.state import State
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    if 'name' not in data:
        error_m = ' Missing name'
        return jsonify(error_m), 400
    obj = Amenity(**data)
    obj.save()
    return jsonify(obj.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def put_state(amenity_id):
    """puts the diccionary in the test"""
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    else:
        obj = storage.get(Amenity, amenity_id)
        if obj is None:
            return abort(404)
        else:
            obj.name = data['name']
            obj.save()
            return jsonify(obj.to_dict()), 200
