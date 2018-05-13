# -*- coding: utf-8 -*-

from aaweb import app

import aaweb.views.login
import aaweb.views.static
import aaweb.views.gallery
import aaweb.views.destinations
import aaweb.views.investors

if app.debug:
    import aaweb.views.debug