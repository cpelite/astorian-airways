# -*- coding: utf-8 -*-

from flask import render_template, abort
from aaweb import app, default_timezone
from aaweb.models import Plane, PlaneLayout, RouteAssignment

import arrow
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
from datetime import datetime

@app.route('/gallery/fleet.html')
def view_fleet():
    planes = Plane.select().order_by(Plane.registration)
    return render_template('gallery/fleet.html', planes=planes)


@app.route('/gallery/planes/<registration>.html')
def gallery_plane(registration):
    try:
        plane = Plane.get(Plane.registration == registration.upper())
        return render_template('gallery/plane.html', plane = plane)
    except Exception as e:
        if isinstance(e, Plane.DoesNotExist):
            abort(404)
        abort(500)

@app.route('/gallery/live/map.png')
def gallery_live_map():


    # basic background
    img = Image.open("static/imgs/flightmap.png")

    # font
    font = ImageFont.truetype("static/fonts/oxygen-mono-v4-latin-regular.ttf", 10)

    draw = ImageDraw.Draw(img)
    draw.text((5, img.size[1] - 15), arrow.now(default_timezone).strftime('%H:%M %d.%m.%y (%a)'), (26, 26, 26), font=font) # timestamp

    for plane in Plane.select():
        flying, coordinates, code = plane.current_position()

        if flying:
            ra = RouteAssignment.get_by_flight_number(code) 
            draw.line(ra.route.get_coordinates(), fill=(83, 83, 83))# flight - yellow: (252, 193, 5)
            draw.ellipse((coordinates[0] - 3, coordinates[1] - 3, coordinates[0] + 5, coordinates[1] + 5), fill = (178, 217, 35)) # dot
            draw.text((coordinates[0]+10, coordinates[1]-12), plane.registration, (125, 125, 125), font=font) # registration'
            draw.text((coordinates[0]+10, coordinates[1]+2), ra.get_flight_number(with_spaces=False), (125, 125, 125), font=font)

    io = BytesIO()
    img.save(io, format='png') # PNG format
    io.seek(0)
    return io.read(), 200, {'Content-type': 'image/png', 'Cache-Control' : 'public, max-age=180, must-revalidate', 'Last-Modified' : datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")}
