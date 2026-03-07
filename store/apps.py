from django.apps import AppConfig
from mongoengine import connect
from django.conf import settings

class StoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'store'

    def ready(self):
        # Connect MongoEngine to local MongoDB
        if not connect._connections:
            connect(host=settings.MONGO_URL, alias='default')