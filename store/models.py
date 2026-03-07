# store/models.py
from mongoengine import Document, StringField, DecimalField, ListField, DateTimeField
from datetime import datetime

class Product(Document):
    name = StringField(max_length=255, required=True)
    description = StringField()
    price = DecimalField(required=True, precision=2)
    tags = ListField(StringField(), default=[])
    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return self.name

    meta = {'db_alias': 'default'}

# Example: Add more models if needed
class Customer(Document):
    first_name = StringField(max_length=100, required=True)
    last_name = StringField(max_length=100, required=True)
    email = StringField(max_length=255, required=True, unique=True)
    phone = StringField(max_length=20)
    created_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    meta = {
        'collection': 'customers',
        'ordering': ['-created_at']
    }

class Order(Document):
    customer = StringField(required=True)  # Store customer ID or email
    products = ListField(StringField())   # Store product IDs or names
    total_price = DecimalField(required=True, precision=2)
    status = StringField(default="pending")  # e.g., pending, shipped, delivered
    created_at = DateTimeField(default=datetime.utcnow)

    def __str__(self):
        return f"Order for {self.customer} - {self.status}"

    meta = {
        'collection': 'orders',
        'ordering': ['-created_at']
    }