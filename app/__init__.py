"""
Entry point for app
"""

from flask import Flask

from flask_bootstrap import Bootstrap

from .frontend import frontend
from .nav import nav

def create_app():
    """
    Application Factory - see http://flask.pocoo.org/docs/patterns/appfactories/
    """

    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'NOT SO SECRET'

    # https://pythonhosted.org/Flask-Bootstrap/
    Bootstrap(app)

    # Load blueprints
    # http://flask.pocoo.org/docs/0.12/blueprints/

    # Website
    app.register_blueprint(frontend)

    # http://pythonhosted.org/flask-nav/
    nav.init_app(app)

    return app
