#!/usr/bin/python3
"""API status"""


from flask import jsonify
from api.v1.views import app_views


@app_views.route("/status", strict_slashes=False)
def ViewStatus():
    """returns a json message"""
    return jsonify({"status": "OK"})
