from flask import Flask
from app.routes import api_blueprint
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    
    # Register API routes
    app.register_blueprint(api_blueprint)

    return app
