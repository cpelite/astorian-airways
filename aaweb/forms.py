# -*- coding: utf-8 -*-

import re
from random import shuffle
from datetime import date

from flask import request, render_template, redirect, url_for, session, abort
from aaweb.models import Account
from aaweb.wraps import require_login
from aaweb import app, default_timezone


email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
user_pattern = re.compile(r"(^[a-zA-Z0-9\-_.]+$)")

@app.route('/register', methods=['POST'])
def registration_handler():
    """ Creates a new account request """

     # already logged in
    if 'aid' in session:
        abort(401)

    errors = []

    # data gathering
    tid = request.form.get('tid')
    username = request.form.get('username')
    password = request.form.get('password')
    email = request.form.get('email')
    role = request.form.get('type')

    try:
        role = Account.get_role_number(role)
    except:
        errors.append("You really should select an appropriate account type dude")

    if not username:
        errors.append("Oh dear, you didn't enter an username")
    elif len(username) < 4 or len(username) > 25:
        errors.append("Look at that, your username must be at least 4 characters and at most 25 characters long")
    elif not re.match(user_pattern, username):
        errors.append("Just choose an username composed of alphanumerical letters, dashes, underscores and points, would you?")

    if not password:
        errors.append("Seems like you didn't enter a password")
    elif len(password) < 5 or len(password) > 25:
        errors.append("Your password must be longer than just 4 characters and at most 25 characters long")

    if not email:
        errors.append("No, no - you honestly do need an email address")
    elif not re.match(email_pattern, email):
        errors.append("Come on, your email address is not valid")

    if not tid:
            errors.append("Brother, your TID is missing")

    if len(errors) == 0: # only check if there are no prior errors found
        if tid:
            try:
                tid = int(tid)
            except:
                errors.append("Your TID looks pretty fishy")

    # everything is okay? Setup new user and init password
    # ...timing attacks aren't actually much of a deal here :P
    if len(errors) == 0:
        try:
            a = Account.create_and_salt( username = username,
                            citizen = tid,
                            password = password,
                            email = email,
                            role = role
                          )

        except Exception as e:
            print(e)
            errors.append("Seems like your username is already used")

    # shuffle errors to obfuscate the order of checks :)
    if len(errors) > 0: 
        shuffle(errors)

    return render_template('registration/result.html', errors=errors)

@app.route('/edituser', methods=['POST'])
@require_login
def edit_handler():
    """ Handles edit request of a single account """

    # already logged in
    if not 'aid' in session:
        return redirect(url_for("account_home"))

    reason = "password"
    try:
        a = Account.get(Account.aid == session["aid"])

        # wrong password
        if not a.check_password(request.form['password']):
            app.logger.info('refused edit of %s (#%i) with password "%s"'  % (a.username, a.aid, request.form['password']) )
            raise Exception

        # non equal passwords
        if not request.form['wpassword1'] == request.form['wpassword2']:
            app.logger.info('refused password edit of %s (#%i) because "%s" != "%s"'  % (a.username, a.aid, request.form['wpassword1'], request.form['wpassword2']) )
            reason = "no-match"
            raise Exception

        # password edit wish?
        if len(request.form['wpassword1']) > 0:
            a.password, a.salt = Account.create_salted_password(request.form['wpassword1'])

        a.save()

        return redirect(url_for("account_home"))

    except: # edit failure
        return render_template('account/edit_error.html', reason=reason) 

@app.route('/login', methods=['POST'])
def login_handler():
    """ Checks and performs login """


    reason = "credentials"
    try:
        a = Account.get(Account.username == request.form['username'])

        # wrong password
        if not a.check_password(request.form['password']):
            app.logger.info('refused login of %s (#%i) with password "%s"'  % (a.username, a.aid, request.form['password']) )
            raise Exception

        # not activated
        if not a.is_active:
            reason = "activated"
            raise Exception

        # no days left
        if a.paid_until < date.today(default_timezone):
            reason = "payment"
            raise Exception

        # successful login
        session['username'] = a.username
        session['role'] = a.role
        session['aid'] = a.aid
        app.logger.info("successful login of %s (#%i)"  % (a.username, a.aid) )
        return redirect(url_for("account_home"))

    except: # login failure
        return render_template('login/error.html', reason=reason) 

@app.route('/logoff')
@require_login
def logoff_handler():
    """ Checks and performs logoff """

    session.pop('aid', None)
    session.pop('role', None)
    session.pop('username', None)
    return redirect(url_for("home"))