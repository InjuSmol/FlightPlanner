from mongoengine import Document, StringField, IntField

class Airport(Document):
    code = StringField(required=True)
    latitudeDegrees = IntField(required=True)
    latitudeMinutes = IntField(required=True)
    longitudeDegrees = IntField(required=True)
    longitudeMinutes = IntField(required=True)
