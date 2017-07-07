# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# Configure your wsgi here.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thesis.settings")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
