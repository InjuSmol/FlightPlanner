from flask import Blueprint
from controllers.tripController import add_stop, get_trip, calculate_trip_distance

trip_bp = Blueprint('trips', __name__)

trip_bp.route('/add-stop', methods=['POST'])(add_stop)
trip_bp.route('/<trip_id>', methods=['GET'])(get_trip)
trip_bp.route('/<trip_id>/distance', methods=['GET'])(calculate_trip_distance)
