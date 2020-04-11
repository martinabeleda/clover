from clover import api, create_app, db
from clover.resources import Categories, Transactions
from flask_testing import TestCase


class TestEndpoints(TestCase):
    def create_app(self):
        """Create a SQLite db from scratch"""
        api.add_resource(Categories, "/categories")
        api.add_resource(Transactions, "/transactions")
        config = {
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True,
        }
        return create_app(config)

    def setUp(self):
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        """Clear the db"""
        db.session.remove()
        db.drop_all()

    def test_server_is_runnning(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_get_categories(self):
        response = self.client.get("/categories")
        self.assertEqual(response.status_code, 200)

    def test_post_categories(self):
        data = {"name": "groceries", "display_name": "Groceries"}
        response = self.client.post("/categories", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)

    def test_get_transactions(self):
        response = self.client.get("/transactions")
        self.assertEqual(response.status_code, 200)

    def test_post_transaction(self):
        data = {
            "transaction_type": "Purchase",
            "payee": "Woolworths",
            "total": 100.0,
            "category_name": "groceries",
            "id": 2,
            "description": "Woolworths Crows Nest",
            "time": "2020-03-31T12:58:34",
        }
        response = self.client.post("/transactions", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)
