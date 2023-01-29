
# External Imports
from flask_nav import Nav
from flask_nav.elements import *

nav = Nav()

def register_navbar(app):
    nav.register_element('top',
         Navbar(
            View('Home', '.home'),
            View('Hobbies', '.home')
        )
    )
def initialize_navbar(app):
    nav.init_app(app)
