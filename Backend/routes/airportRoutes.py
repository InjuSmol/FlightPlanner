from flask import Blueprint
from controllers.airportController import get_airports

airport_bp = Blueprint('airports', __name__)

airport_bp.route('/', methods=['GET'])(get_airports)
