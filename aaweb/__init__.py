# -*- coding: utf-8 -*-

import os
from datetime import timedelta
from flask import Flask, session

default_timezone = 'Europe/Berlin'

app = Flask(__name__, static_folder='../static', static_url_path='/static', template_folder="../templates/")

app.permanent_session_lifetime = timedelta(minutes=60)

app.config.update(
    SESSION_COOKIE_NAME = "AAsession",
    ERROR_LOG_FILE = "%s/app.log" % os.environ.get('OPENSHIFT_LOG_DIR', 'logs')
)

@app.before_request
def session_activity():
  session.modified = True

@app.route('/robots.txt')
def serve_robots():
    return 'User-agent: *\nDisallow: /'

# VIEWS
import aaweb.views
import aaweb.forms

# API
import aaweb.api

# additional functionalities
import aaweb.error
import aaweb.log
