# -*- coding: utf-8 -*-

import logging
from flask import request, session
from aaweb import app

class ContextualFilter(logging.Filter):
    def filter(self, lr):
        lr.url = request.path
        lr.method = request.method
        lr.ip = request.environ.get("REMOTE_ADDR")
        lr.user_id = session.get('aid',0)
        return True

# init logger
context_provider = ContextualFilter()
app.logger.addFilter(context_provider)
handler = logging.StreamHandler()

log_format = '%(levelname)s [%(asctime)s] %(ip)s "%(method)s %(url)s" #%(user_id)s %(message)s'
formatter = logging.Formatter(log_format)

handler.setFormatter(formatter)
app.logger.addHandler(handler)

# enable error log in none-debug mode
if not app.debug:
    formatter = logging.Formatter('''
Time: %(asctime)s
Level: %(levelname)s
Method: %(method)s
Path: %(url)s
IP: %(ip)s
User ID: %(user_id)s

Message: %(message)s

---------------------''')

    # ERROR fs logging
    if app.config.get("ERROR_LOG_FILE"):
        #print("Logging app internals to %s ..." % app.config["ERROR_LOG_FILE"])
        file_handler = logging.FileHandler(filename=app.config["ERROR_LOG_FILE"], mode='a', encoding='utf8', delay=0)
        file_handler.setLevel(logging.WARNING)
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)