# -*- coding: utf-8 -*-

from aaweb import app
from aaweb.api import api_json_error, api_json_response
from aaweb.api.flight import create_route_assignment_data
from aaweb.models import RouteAssignment, Airport
from peewee import SQL

def create_airport_data(airport, with_flights=False):
    """ Creates dict with needed information of given Airport instance """

    data = { 'city' : airport.city, 'name' : airport.name, 'code' : airport.code }

    if with_flights:
        data.update({ 'departures' : [], 'arrivals' : []})

        for r in airport.departures:
            for ra in RouteAssignment.select().where( SQL('route_id = %s', r.id) ):
                data['departures'].append(create_route_assignment_data(ra, from_location=False))

        for r in airport.arrivals:
            for ra in RouteAssignment.select().where( SQL('route_id = %s', r.id) ):
                data['arrivals'].append(create_route_assignment_data(ra, to_location=False))

        data.update( { 'inbound_routes' : len(data['arrivals']), 'outbound_routes' : len(data['departures']) } )

    return data


@app.route('/api/airport/<code>', methods = ('GET',))
def api_airport_details(code):

    try:
        ap = Airport.get(Airport.code == code.upper())
    except:
        return api_json_error('No such airport found')
    return api_json_response(create_airport_data(ap, with_flights=True))

@app.route('/api/current/airports', methods = ('GET',))
def api_airports():

    data = []
    for ap in Airport.select():
        data.append(create_airport_data(ap, with_flights=False))
    return api_json_response(data)