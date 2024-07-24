from mongoengine import Document, ListField, ReferenceField
from .Airport import Airport

class Trip(Document):
    stops = ListField(ReferenceField(Airport))
