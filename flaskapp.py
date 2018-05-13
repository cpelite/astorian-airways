#!/usr/bin/env python

import os
from aaweb import app as _app

_app.config.update(
    SECRET_KEY = os.urandom(32),
    HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS','localhost'),
    APP_NAME = os.environ.get('OPENSHIFT_APP_NAME','flask'),
    IP = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1'),
    PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080)),
)

if __name__ == '__main__':
    print("Starting in DEBUG mode ...")

    if not os.environ.get('OPENSHIFT_PYTHON_IP'):
        _app.debug = True
    _app.run()
else:
    app = _app
