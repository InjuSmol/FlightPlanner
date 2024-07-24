from flask import jsonify
from models.Airport import Airport

def get_airports():
    airports = Airport.objects()
    return jsonify(airports), 200
