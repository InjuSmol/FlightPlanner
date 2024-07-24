from flask import request, jsonify
from models.Trip import Trip
from models.Airport import Airport
from utils.distanceCalculator import calculate_distance

def add_stop():
    data = request.get_json()
    trip_id = data.get('tripId')
    airport_code = data.get('airportCode')
    
    trip = Trip.objects.get(id=trip_id)
    airport = Airport.objects.get(code=airport_code)
    trip.stops.append(airport)
    trip.save()
    
    return jsonify(trip), 200

def get_trip(trip_id):
    trip = Trip.objects.get(id=trip_id)
    return jsonify(trip), 200

def calculate_trip_distance(trip_id):
    trip = Trip.objects.get(id=trip_id)
    total_distance = 0
    stops = trip.stops
    for i in range(len(stops) - 1):
        total_distance += calculate_distance(stops[i], stops[i + 1])
    
    return jsonify({'totalDistance': total_distance}), 200
