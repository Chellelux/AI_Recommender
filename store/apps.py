from django.apps import AppConfig
from mongoengine import connect
import os

class StoreConfig(AppConfig):
    name = 'store'

    def ready(self):
        # Only connect if not already connected
        if not connect._connections:
            mongo_uri = os.getenv("MONGO_URI")
            connect(host=mongo_uri)