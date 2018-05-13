# -*- coding: utf-8 -*-

from flask import render_template
from aaweb import app
from aaweb.models import Route, RouteAssignment

@app.route('/about/destinations.html')
def view_destinations():
    active_routes = [route for route in Route.select() if RouteAssignment.select().where(RouteAssignment.route == route).count() > 0]

    print(RouteAssignment.select().where(RouteAssignment.route == active_routes[-1].id).count())
    return render_template('about/destinations.html', active_routes = active_routes)