"""
WSGI config for ecommerce_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

# ecommerce_project/wsgi.py
import os
from django.core.wsgi import get_wsgi_application

# Connect to Mongo safely
from .mongo import mongo_connect
mongo_connect()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce_project.settings")
application = get_wsgi_application()