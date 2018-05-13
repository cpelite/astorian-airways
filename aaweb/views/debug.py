# -*- coding: utf-8 -*-

from flask import render_template, send_from_directory
from aaweb import app

@app.route('/static/js/<path:path>')
def send_js(path):
    return send_from_directory(app.static_folder + '/js', path)

@app.route('/static/fonts/<path:path>')
def send_fonts(path):
    return send_from_directory(app.static_folder + '/fonts', path)

@app.route('/static/css/<path:path>')
def send_css(path):
    return send_from_directory(app.static_folder + '/css', path)

@app.route('/static/imgs/<path:path>')
def send_imgs(path):
    return send_from_directory(app.static_folder + '/imgs', path)
