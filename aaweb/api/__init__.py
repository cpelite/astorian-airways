# -*- coding: utf-8 -*-

from aaweb import app
from flask import json, Response

def api_json_error(msg, status=404):
    """ Central 404 JSON error method """

    return Response('{"error": "%s"}' % msg, status=status, mimetype='application/json')

def api_json_response(data, status=200):
    """ Central JSON return method """

    return Response(json.dumps(data), status=status, mimetype='application/json')

import aaweb.api.plane
import aaweb.api.flight
import aaweb.api.airport
