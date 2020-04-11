from flask import Flask
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from marshmallow import post_load
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.exc import IntegrityError

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


@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
