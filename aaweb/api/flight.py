# -*- coding: utf-8 -*-

from aaweb import app
from aaweb.api import api_json_error, api_json_response
from aaweb.models import RouteAssignment
from flask import url_for

def create_route_assignment_data(ra, from_location=True, to_location=True, flight_number=True):
    """ Creates dict with needed flight information of given RouteAssignment instance """

    departure, arrival = ra.calculate_concrete_datetimes()

    days = []
    if ra.monday:
        days.append('MON')
    if ra.tuesday:
        days.append('TUE')
    if ra.wednesday:
        days.append('WED')
    if ra.thursday:
        days.append('THR')
    if ra.friday:
        days.append('FRI')
    if ra.saturday:
        days.append('SAT')
    if ra.sunday:
        days.append('SUN')

    data = {
        'starting' : departure.strftime("%H:%M"),
        'duration' : ra.route.duration,
        'landing' : arrival.strftime("%H:%M"),
        'days' : days,
    }

    if flight_number:
        fn = ra.get_flight_number(with_spaces=False)
        data.update( { 'flight_number' : fn, 'details' : url_for('api_flight_details', flight_number=fn) })

    if from_location:
        data.update( { 'from' : {
                    'airport' : ra.route.departure.name, 
                    'city' : ra.route.departure.city,
                    'code' : ra.route.departure.code,
                    'detials' : url_for('api_airport_details', code=ra.route.departure.code),
                }
            }
        )

    if to_location:
        data.update( { 'to' : { 
                    'airport' : ra.route.arrival.name,
                    'city' : ra.route.arrival.city,
                    'code' : ra.route.arrival.code,
                    'detials' : url_for('api_airport_details', code=ra.route.arrival.code),
                }
            }
        )

    return data


@app.route('/api/flight/<flight_number>', methods = ('GET',))
def api_flight_details(flight_number):

    try:
        ra = RouteAssignment.get_by_flight_number(flight_number.upper())
    except:
        return api_json_error('No such flight found')

    data = create_route_assignment_data(ra, flight_number=False)
    data.update({ 'flight_number' : flight_number.upper() })

    return api_json_response(data=data)


