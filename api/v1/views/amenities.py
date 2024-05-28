#!/usr/bin/python3
"""Create a new view for amenity objects
that handles all default RESTFul API actions"""

from flask import Flask, abort, request
from api.v1.views import app_views
from os import name
from models.amenity import Amenity


@app_views.route('amenities', methods=['GET'], strict_slashes=False)
def Get_Amenity():
    """Retrieves the list of all Amenity objects"""
    response = [
        amenity.to_dict() for amenity in storage.all(Amenity).values()
    ]
    return jsonify(response)


@app_views.route('amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def Getting_Amenity(amenity_id):
    """Retrieves a Amenity object"""
    AmenityObj = storage.get(Amenity, amenity_id)
    if AmenityObj is None:
        abort(404)
    return jsonify(AmenityObj.to_dict())


@app_views.route('amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def Deleting__Amenity():
    """to delete an Amenity object"""
    AmenityObj = storage.get(Amenity, amenity_id)
    if AmenityObj is None:
        abort(404)
    storage.delete(AmenityObj)
    storage.save()
    return jsonify({}), '200'


@app_views.route('amenities', methods=['POST'],
                 strict_slashes=False)
def Posting_Amenity():
    """Creates an Amenity"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    if "name" not in response:
        abort(400, {'Missing name'})
    AmenityObj = City(name=response['name'])
    storage.new(AmenityObj)
    storage.save()
    return jsonify(AmenityObj.to_dict()), '201'


@app_views.route('amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def Putting():
    """Updates a Amenity object"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    AmenityObj = storage.get(Amenity, amenity_id)
    if AmenityObj is None:
        abort(404)
    IgnoreKeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in IgnoreKeys:
            setattr(AmenityObj, key)
    storage.save()
    return jsonify(AmenityObj.to_dict()), '200'
