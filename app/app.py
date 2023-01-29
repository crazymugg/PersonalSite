# Standard Imports

# External Imports
from flask import Flask
from flask_bootstrap import Bootstrap

# Local Imports
from app.extensions.views import create_views
from app.extensions.navbar import register_navbar, initialize_navbar

class Factory:
    def create_app():
        app = Flask(__name__)
        Bootstrap(app)        
        create_views(app)
        register_navbar(app)
        initialize_navbar(app)

        return app


    def run(app):
        app.run()