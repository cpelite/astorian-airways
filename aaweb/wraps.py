# -*- coding: utf-8 -*-

from flask import abort, session
from functools import wraps

def require_role(*roles):
    def wrapper(f):
        @wraps(f)
        def require_wrapped(*args, **kwargs):
            if session.get("role", None) not in roles:
                return abort(401)
            return f(*args, **kwargs)
        return require_wrapped
    return wrapper



def require_login(f):
    @wraps(f)
    def login_wrapped(*args, **kwargs):
        if session.get("role") is None:
            abort(401)
        return f(*args, **kwargs)
    return login_wrapped
