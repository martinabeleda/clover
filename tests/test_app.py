from flask import Flask
from flask_testing import TestCase
import requests
from transactions.app import app


class StartingTestCase(TestCase):
    def setUp(self):
        self.client = app.test_client()

    def tearDown(self):
        pass

    def create_app(self):
        """
        This is a requirement for Flask-Testing
        """
        app = Flask(__name__)
        app.config["TESTING"] = True
        self.base_url = "http://localhost:5000"
        return app

    def test_api_is_up_and_running(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)

    def test_get_transactions(self):
        response = requests.get(f"{self.base_url}/transactions")
        self.assert200(response)
        self.assertIn("data", response.json())
        self.assertIsInstance(response.json()["data"], list)

    def test_get_categories(self):
        response = requests.get(f"{self.base_url}/categories")
        self.assert200(response)
        self.assertIn("data", response.json())
        self.assertIsInstance(response.json()["data"], list)

    def test_get_category_types(self):
        response = requests.get(f"{self.base_url}/category-types")
        self.assert200(response)
        self.assertIn("data", response.json())
        self.assertIsInstance(response.json()["data"], list)
