#!/usr/bin/python3
"""task-4"""
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status')
def json_return():
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def count_stats():
    from models.amenity import Amenity
    from models.city import City
    from models.place import Place
    from models.review import Review
    from models.state import State
    from models.user import User
    from models import storage
    classes = {"amenities": Amenity, "cities": City, "places": Place,
               "reviews": Review, "states": State, "users": User}
    r_dict = {}
    for i in classes:
        r_dict["{}".format(i)] = storage.count(classes[i])
    return jsonify(r_dict)
