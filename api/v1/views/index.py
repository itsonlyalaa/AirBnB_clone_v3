#!/usr/bin/python3
"""API status"""


from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def ViewStatus():
    """returns a json message"""
    return jsonify({"status": "OK"})


@app_views.route("/stats", strict_slashes=False)
def viewStats():
    """retrieves the number of each object by type"""
    return jsonify({
        "amenities": models.storage.count(Amenity),
        "cities": models.storage.count(City),
        "places": models.storage.count(Place),
        "reviews": models.storage.count(Review),
        "states": models.storage.count(State),
        "users": models.storage.count(User)
    })
