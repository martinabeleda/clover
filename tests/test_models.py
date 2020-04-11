from datetime import datetime
from unittest import TestCase

from clover.models import Category, Transaction


class TestCategory(TestCase):
    def test_create_category(self):
        category = Category(name="public_transport", display_name="Public Transport")
        category_string = repr(category)
        self.assertIn("Category", category_string)
        self.assertIn("name=public_transport", category_string)
        self.assertIn("display_name=Public Transport", category_string)


class TestTransaction(TestCase):
    def test_create_transaction(self):
        transaction = Transaction(
            time=datetime.fromisoformat("2020-03-31T12:58:34+11:00"),
            transaction_type="Purchase",
            payee="Woolworths",
            description="Woolworths Crows Nest",
            total=100.00,
            category_name="groceries",
        )
        transaction_string = repr(transaction)
        self.assertIn("Transaction", transaction_string)
        self.assertIn("transaction_type=Purchase", transaction_string)
        self.assertIn("payee=Woolworths", transaction_string)
        self.assertIn("category_name=groceries", transaction_string)
        self.assertIn("total=100.0", transaction_string)
