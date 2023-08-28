#!/usr/bin/python3
"""task-11"""
from models import storage
from models.place import Place
from models.user import User
from models.city import City
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('/places/<place_id>', methods=['GET'])
def places_to_dict(place_id=None):
    """ Users to dictionary """
    lista = []
    for i in storage.all(Place):
        lista.append(storage.all(Place)[i].to_dict())
    if place_id is None:
        return jsonify(lista)
    else:
        for i in lista:
            if i['id'] == place_id:
                return jsonify(i)
        return abort(404)


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def list_places_by_city(city_id):
    """ List places by city """
    lista = []
    for i in storage.all(Place):
        lista.append(storage.all(Place)[i].to_dict())
    for i in lista:
        if i['city_id'] == city_id:
            return jsonify(i)
    return abort(404)


@app_views.route('/places/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """ Delete user """
    obj = storage.get(Place, place_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/cities/<city_id>/places', methods=['POST'])
@app_views.route('/cities/<city_id>/places/', methods=['POST'])
def post_place(city_id):
    """ Post place """
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    elif 'user_id' not in data:
        error_m = ' Missing user_id'
        return jsonify(error_m), 400
    elif 'city_id' not in data:
        error_m = ' Missing city_id'
        return jsonify(error_m), 400
    elif 'name' not in data:
        error_m = ' Missing name'
        return jsonify(error_m), 400
    else:
        obj = Place()
        obj.user_id = data['user_id']
        obj.city_id = data['city_id']
        obj.name = data['name']
        obj.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/places/<place_id>', methods=['PUT'])
def put_place(place_id):
    """ Put place """
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
