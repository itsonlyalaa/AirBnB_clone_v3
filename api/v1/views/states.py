#!/usr/bin/python3
"""Create a new view for State objects
that handles all default RESTFul API actions"""

from flask import Flask, abort, request
from api.v1.views import app_views
from os import name
from models.state import State


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def Get_State():
    """retrieves an object into a valid JSON"""
    obj = storage.all('State')
    My_list = []
    for state in obj.values():
        My_list.append(state.to_dict())
    return jsonify(My_list)


@app_views.route('/states/<string:stateid>', methods=['GET'],
                 strict_slashes=False)
def GettingID():
    """Updates a State object id"""
    obj = storage.get('State', 'state_id')
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def Deleting():
    """to delete an object"""
    StateObj = storage.get(State, state_id)
    if stateObj is None:
        abort(404)
    storage.delete(StateObj)
    storage.save()
    return jsonify({}), '200'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def Posting():
    """Creates a State"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    if "name" not in response:
        abort(400, {'Missing name'})
    StateObj = State(name=response['name'])
    storage.new(StateObj)
    storage.save()
    return jsonify(StateObj.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def Putting():
    """Updates a State object"""
    response = request.get_json()
    if response is None:
        abort(400, {'Not a JSON'})
    StateObj = storage.get(State, state_id)
    if StateObj is None:
        abort(404)
    IgnoreKeys = ['id', 'created_at', 'updated_at']
    for key in response.items():
        if key not in IgnoreKeys:
            setattr(StateObj, key)
    storage.save()
    return jsonify(StateObj.to_dict()), '200'
