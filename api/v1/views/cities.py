#!/usr/bin/python3
"""task-8"""
from models import storage
from models.city import City
from models.state import State
from flask import jsonify, abort, request
from api.v1.views import app_views


@app_views.route('states/<state_id>/cities/', methods=['GET'])
def get_cities_of_an_id(state_id):
    """searchs in cities and put it in a list if state_id == cities.state_id"""
    state = storage.get("State", state_id)
    if state is None:
        return abort(404)
    cities = []
    for city in state.cities:
        cities.append(city.to_dict())
    return jsonify(cities)


@app_views.route('/cities/<city_id>', methods=['GET'])
def gets_city(city_id):
    """gets the city with the id"""
    city = storage.get(City, city_id)
    if city is None:
        return abort(404)
    else:
        return jsonify(city.to_dict())
    

@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """it deletes from objects"""
    fetched_obj = storage.get(City, city_id)
    if fetched_obj is None:
        abort(404)
    storage.delete(fetched_obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def post_city(state_id):
    """search and create a state"""
    obj_data = request.get_json()
    if not obj_data:
        abort(400, "Not a JSON")
    if "name" not in obj_data:
        abort(400, "Missing name")
    state = storage.get(State, state_id)
    """State was a str it needs to be a class"""
    if state is None:
        abort(404)
    obj_data['state_id'] = state.id
    obj = City(**obj_data)
    storage.new(obj)
    storage.save()
    return jsonify(obj.to_dict()), 201

@app_views.route('/cities/<city_id>', methods=['PUT'])
def put_city(city_id):
    """puts the diccionary in the test"""
    data = request.get_json()
    if not data:
        error_m = 'Not a JSON'
        return jsonify(error_m), 400
    else:
        obj = storage.get(City, city_id)
        if obj is None:
            return abort(404)
        else:
            obj.name = data['name']
            obj.save()
            return jsonify(obj.to_dict()), 200
