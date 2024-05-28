#!/usr/bin/python3
"""Create a new view for city objects
that handles all default RESTFul API actions"""

from flask import Flask, abort, request
from api.v1.views import app_views
from os import name
from models.state import State
from models.city import City


@app_views.route('/status/<state_id>/cities"', methods=['GET'],
                 strict_slashes=False)
def Get_City(state_id):
    """Retrieves the list of all City objects of a State"""
    obj = storage.get(State, state_id)
    if state is None:
        abort(404)
        return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def Getting_City(city_id):
    """Updates a city object"""
    CityObj = storage.get(City, city_id)
    if CityObj is None:
        abort(404)
    return jsonify(CityObj.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'],
                 strict_slashes=False)
def Deleting__City():
    """to delete an city object"""
    CityObj = storage.get(City, city_id)
    if CityObj is None:
        abort(404)
    storage.delete(CityObj)
    storage.save()
    return jsonify({}), '200'


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def Posting_City():
    """Creates a City"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    if "name" not in response:
        abort(400, {'Missing name'})
    CityObj = City(name=response['name'])
    storage.new(CityObj)
    storage.save()
    return jsonify(CityObj.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def Putting():
    """Updates a city object"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    CityObj = storage.get(City, city_id)
    if CityObj is None:
        abort(404)
    IgnoreKeys = ['id', 'state_id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in IgnoreKeys:
            setattr(CityObj, key)
    storage.save()
    return jsonify(CityObj.to_dict()), '200'
