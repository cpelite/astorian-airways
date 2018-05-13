# -*- coding: utf-8 -*-

from flask import session, render_template, redirect, url_for
from aaweb import app

@app.route('/login.html')
def login():
    if not session.get("aid"):
        return render_template('login/main.html')
    return redirect(url_for("account_home")) 