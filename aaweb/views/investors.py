# -*- coding: utf-8 -*-

from flask import render_template
from aaweb import app
from aaweb.models import Company


@app.route('/investor/relations.html')
def view_investor():
    companies = Company.select()
    return render_template('investor.html',  companies=companies)