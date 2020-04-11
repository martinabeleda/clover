from clover import api, create_app, db
from clover.models import CategoryModel, TransactionModel
from clover.resources import Categories, Category, Transaction, Transactions
from flask_testing import TestCase


class TestEndpoints(TestCase):
    def create_app(self):
        """Create a SQLite db from scratch"""
        api.add_resource(Category, "/category")
        api.add_resource(Categories, "/categories")
        api.add_resource(Transaction, "/transaction")
        api.add_resource(Transactions, "/transactions")
        config = {
            "SQLALCHEMY_DATABASE_URI": "sqlite://",
            "SQLALCHEMY_TRACK_MODIFICATIONS": False,
            "TESTING": True,
        }
        return create_app(config)

    def setUp(self):
        self.client = self.app.test_client()
        db.drop_all()
        db.create_all()

        self.assertFalse(CategoryModel.query.all())
        self.assertFalse(TransactionModel.query.all())

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

    def test_post_category(self):
        data = {"name": "groceries", "display_name": "Groceries"}
        response = self.client.post("/category", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)

    def test_post_category_with_duplicate_name(self):
        data_1 = {"name": "investments", "display_name": "Foo"}
        response = self.client.post("/category", json=data_1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data_1)

        data_2 = {"name": "investments", "display_name": "Bar"}
        response = self.client.post("/category", json=data_2)
        self.assertEqual(response.status_code, 409)
        self.assertIn("Category already exists", response.json["msg"])
        self.assertEqual(response.json["data"], data_1)

    def test_post_category_with_duplicate_display_name(self):
        data_1 = {"name": "foo", "display_name": "Foo"}
        response = self.client.post("/category", json=data_1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data_1)

        data_2 = {"name": "bar", "display_name": "Foo"}
        response = self.client.post("/category", json=data_2)
        self.assertEqual(response.status_code, 409)
        self.assertIn("Category already exists", response.json["msg"])
        self.assertEqual(response.json["data"], data_1)

    def test_get_transactions(self):
        response = self.client.get("/transactions")
        self.assertEqual(response.status_code, 200)

    def test_post_transaction(self):

        # First, create a category
        data = {"name": "groceries", "display_name": "Groceries"}
        response = self.client.post("/category", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)

        # Now assign a transaction to that category
        data = {
            "transaction_type": "Purchase",
            "payee": "Woolworths",
            "total": 100.0,
            "category_name": "groceries",
            "id": 2,
            "description": "Woolworths Crows Nest",
            "time": "2020-03-31T12:58:34",
        }
        response = self.client.post("/transaction", json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, data)

    def test_post_transaction_with_nonextant_category(self):
        data = {
            "transaction_type": "Purchase",
            "payee": "Woolworths",
            "total": 100.0,
            "category_name": "groceries",
            "id": 2,
            "description": "Woolworths Crows Nest",
            "time": "2020-03-31T12:58:34",
        }
        response = self.client.post("/transaction", json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Tried to create a transaction with nonextant category", response.json["msg"])
        self.assertEqual(response.json["data"], data)
