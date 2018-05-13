# -*- coding: utf-8 -*-

from aaweb import app
from aaweb.api import api_json_error, api_json_response
from aaweb.models import Plane, PlaneLayout
from flask import url_for

@app.route('/api/current/planes', methods = ('GET',))
def api_current_planes():

    data = []
    for plane in Plane.select():
        details = {}

        flying, coordinates, code = plane.current_position()

        details = {
            'name' : plane.alias,
            'manufacturer' : plane.manufacturer,
            'aircraft' : plane.aircraft,
            'registration' : plane.registration,
            'situation' : 'IN-FLIGHT' if flying else 'ON-GROUND',
            'current_coordinates' : { 
                'lat' : coordinates[0], 
                'lon' : coordinates[1],
                'map' : url_for('static', filename='imgs/flightmap.png'),
                'flight' if flying else 'airport' : code,
            },
            'details' : url_for('api_plane_details', registration=plane.registration),
        }
        data.append(details)
    return api_json_response(data)

@app.route('/api/plane/<registration>', methods = ('GET',))
def api_plane_details(registration):

    try:
        plane = Plane.get(Plane.registration == registration.upper())
    except:
        return api_json_error('No such plane found')

    flying, coordinates, code = plane.current_position()

    data = {
        'registration' : plane.registration,
        'name' : plane.alias,
        'aircraft' : plane.aircraft,
        'manufacturer' : plane.manufacturer,
        'crew' : {
            'pilots' : plane.pilots,
            'flight_attendants' : plane.layout.flight_attendants,
            'total' : plane.layout.flight_attendants + plane.pilots,
        },
        'passangers': { 
            'economy' : plane.layout.economy_class, 
            'business' : plane.layout.business_class, 
            'first' : plane.layout.first_class,
            'total' : plane.layout.economy_class + plane.layout.business_class + plane.layout.first_class,
        },
        'imgs' : { 
            'cabin' : url_for('static', filename='imgs/layout/%s' % plane.layout.picture),
            'livery' : url_for('static', filename='imgs/planes/%s' % plane.picture),
        },
        'situation' : 'IN-FLIGHT' if flying else 'ON-GROUND',
        'current_coordinates' : { 
            'lat' : coordinates[0], 
            'lon' : coordinates[1],
            'map' : url_for('gallery_live_map'),
            'flight' if flying else 'airport' : code,
        }

    }

    return api_json_response(data)
