from datetime import datetime

from clover import api, create_app, db
from clover.models import Category, Transaction
from clover.resources import Categories, Transactions
from flask_testing import TestCase
from sqlalchemy.exc import IntegrityError


class TestTransactionsDB(TestCase):
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
        """Create a SQLite db from scratch"""
        db.drop_all()
        db.create_all()

        # Ensure we're not pulling in state from a previous session
        self.assertFalse(Category.query.all())
        self.assertFalse(Transaction.query.all())

    def tearDown(self):
        """Clear the db"""
        db.session.remove()
        db.drop_all()

    def test_add_and_remove_category(self):
        """Test adding and removing a new category"""
        category = Category(name="public_transport", display_name="Public Transport")
        db.session.add(category)
        db.session.commit()

        # Test that the category has been successfuly created
        self.assertIsNotNone(Category.query.get("public_transport"))

        # Delete the category
        db.session.delete(category)
        db.session.commit()
        self.assertIsNone(Category.query.get(category.name))

    def test_adding_conflicting_categories(self):
        """Ensure that we get an exception when adding categories with conficting names"""
        category_1 = Category(name="public_transport", display_name="Public Transport")
        category_2 = Category(name="public_transport", display_name="Public Transport")
        db.session.add(category_1)
        db.session.add(category_2)

        with self.assertRaises(IntegrityError) as context:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise

        self.assertTrue("UNIQUE constraint failed" in str(context.exception))
        self.assertFalse(Category.query.all())

    def test_add_category_with_missing_name(self):
        category = Category(display_name="Investments")
        db.session.add(category)

        with self.assertRaises(IntegrityError) as context:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise

        self.assertTrue("NOT NULL constraint failed: categories.name" in str(context.exception))
        self.assertFalse(Category.query.all())

    def test_add_category_with_missing_display_name(self):
        category = Category(name="investments")
        db.session.add(category)

        with self.assertRaises(IntegrityError) as context:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise

        self.assertTrue("NOT NULL constraint failed: categories.display_name" in str(context.exception))
        self.assertFalse(Category.query.all())

    def test_add_transaction(self):
        """Test adding a new transaction and mapping that to a category"""

        # First, create a category
        category = Category(name="groceries", display_name="Groceries")
        db.session.add(category)
        db.session.commit()

        # Now, create the transaction
        transaction = Transaction(
            time=datetime.fromisoformat("2020-03-31T12:58:34+11:00"),
            transaction_type="Purchase",
            payee="Woolworths",
            description="Woolworths Crows Nest",
            total=100.00,
            category_name="groceries",
        )
        db.session.add(transaction)
        db.session.commit()

        # Check that the transaction has been created sucessfully
        result = Transaction.query.get(transaction.id)
        self.assertTrue(result)
        self.assertEqual(result, transaction)

        # Check that we can access it by it's category
        result = category.transactions[0]
        self.assertEqual(result, transaction)

    def test_add_transaction_with_nonextant_category(self):
        # Now, create the transaction
        transaction = Transaction(
            time=datetime.fromisoformat("2020-03-31T12:58:34+11:00"),
            transaction_type="Purchase",
            payee="Woolworths",
            description="Woolworths Crows Nest",
            total=100.00,
            category_name="groceries",
        )
        db.session.add(transaction)
        with self.assertRaises(IntegrityError) as context:
            try:
                db.session.commit()
            except:
                db.session.rollback()
                raise

        self.assertTrue("FOREIGN KEY constraint failed" in str(context.exception))
        self.assertFalse(Transaction.query.all())
