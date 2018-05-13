# -*- coding: utf-8 -*-

from flask import render_template
from aaweb import app

# HOME
@app.route('/app')
@app.route('/')
@app.route('/index.html')
def home():
    return render_template('home.html')

########
# ABOUT
#

@app.route('/about/ceo.html')
def view_ceo():
    return render_template('about/ceo.html')

@app.route('/about/api.html')
def view_api():
    return render_template('about/api.html')

@app.route('/about/legal.html')
def view_legal():
    return render_template('about/legal.html')

@app.route('/jobs.html')
def view_jobs():
    return render_template('about/jobs.html')
#
#
########

########
# SERVICES
#

# VIP
@app.route('/business/shuttle.html')
def view_vip():
    return render_template('vip.html')

# BUSINESS
@app.route('/services/business/cabin.html')
def view_business_cabin():
    return render_template('services/business_cabin.html')

@app.route('/services/business/lounge.html')
def view_business_lounge():
    return render_template('services/lounge.html')

# ECONOMY
@app.route('/services/economy/cabin.html')
def view_economy_cabin():
    return render_template('services/economy_cabin.html')

#
#
########

########
# MSIC
#

@app.route('/partners.html')
def view_partners():
    return render_template('partners.html')

#
#
########