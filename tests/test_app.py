from flask_testing import TestCase
from transactions import create_app, db


class TestEndpoints(TestCase):
    def setUp(self):
        """Create a SQLite db from scratch"""
        db.create_all()

    def tearDown(self):
        """Clear the db"""
        db.session.remove()
        db.drop_all()

    def create_app(self):
        """Configure the testing app to use SQLite"""
        config = {
            "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True,
        }
        app = create_app(config)
        self.app = app.test_client()
        return app

    def test_placeholder(self):
        pass
