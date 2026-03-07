# store/apps.py
from django.apps import AppConfig
from mongoengine import connect
import os

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        # Connect to MongoDB only if not connected
        if not connect._connections:
            mongo_uri = os.getenv("MONGO_URI")
            if mongo_uri:
                connect(host=mongo_uri, alias='default')
            else:
                raise ValueError("MONGO_URI environment variable not set")