# -*- coding: utf-8 -*-
from random import choice
from flask import current_app, Markup, render_template, request
from werkzeug.exceptions import default_exceptions, HTTPException

from aaweb import app


def error_handler(error):
    """ Centralized error handler """

    if isinstance(error, HTTPException):
        description = error.get_description(request.environ)
        code = error.code
        name = error.name

    else:
        description = "We encountered some problems while trying to fulfill your request"
        code = 500
        name = "Internal Server Error"
        msg = "Request resulted in {}".format(error)
        current_app.logger.error(msg, exc_info=error)


    if code == 404:
      gif = choice(('TEGd412','cufIziI','6AhcU48','ZoVs6'))
    elif code == 401:
      gif = choice(('xmiEPCk','VSS7M0m','CbbQbTi','ugjlfcb'))
    else:
      gif = choice(('VomR345','SCZu6zY','E86gqLG','GeMGOBr'))

    return render_template('errors/generic.html',
                           code=code,
                           name=Markup(name),
                           description=Markup(description),
                           error=error,
                           gif=Markup(gif)), code

# init error handler
for exception in default_exceptions:
    app.register_error_handler(exception, error_handler)
app.register_error_handler(Exception, error_handler)
