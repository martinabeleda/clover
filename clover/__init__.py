from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api
from flask_sqlalchemy import SQLAlchemy

__version__ = "0.1.0"


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy()
ma = Marshmallow()


def create_app(config: dict) -> Flask:
    """Create and configure a Flask application

    Args:
        config (dict): A dict containing app config where
            the keys are the `app.config["{key}"]` and the
            values are the configuration passed in.

    Returns:
        Flask: A Flask app instance with the configuration
            applied
    """
    for key, value in config.items():
        app.config[key] = value
    db.init_app(app)
    ma.init_app(app)
    app.app_context().push()
    return app
