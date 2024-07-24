from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure your app
app.config['MONGO_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize extensions
mongo = PyMongo(app)

# Register blueprints and other setup
from routes.airportRoutes import airport_bp
from routes.tripRoutes import trip_bp

app.register_blueprint(airport_bp, url_prefix='/api/airports')
app.register_blueprint(trip_bp, url_prefix='/api/trips')

if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG') == 'True')

'''
from flask import Flask
from routes.airportRoutes import airport_bp
from routes.tripRoutes import trip_bp
from config.db import initialize_db

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'trip_planner',
    'host': 'localhost',
    'port': 27017
}

initialize_db(app)

app.register_blueprint(airport_bp, url_prefix='/api/airports')
app.register_blueprint(trip_bp, url_prefix='/api/trips')

if __name__ == '__main__':
    app.run(debug=True)
'''
