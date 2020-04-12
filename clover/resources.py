from clover import api, db
from clover.models import CategoryModel, TransactionModel
from clover.schema import CategorySchema, TransactionSchema
from flask_restx import Resource
from sqlalchemy.exc import IntegrityError

_categories_schema = CategorySchema(many=True)
_category_schema = CategorySchema()
_transactions_schema = TransactionSchema(many=True)
_transaction_schema = TransactionSchema()


class Categories(Resource):
    def get(self):
        """Get a list of all transaction catgories"""
        categories = CategoryModel.query.all()
        return _categories_schema.dump(categories)

    def post(self):
        """Create a new transaction category"""
        new_category = _category_schema.load(api.payload)
        db.session.add(new_category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            existing_category = CategoryModel.query.get(new_category.name)
            if not existing_category:
                existing_category = CategoryModel.query.filter_by(display_name=new_category.display_name).first()
            return {"msg": "Category already exists", "data": _category_schema.dump(existing_category)}, 409
        return _category_schema.dump(new_category), 201


class Category(Resource):
    def get(self, name: str):
        """Get a transaction category by name"""
        category = CategoryModel.query.get(name)
        if not category:
            return {"msg": "Category not found."}, 404
        category_result = _category_schema.dump(category)
        transactions_result = _transactions_schema.dump(category.transactions)
        return {"category": category_result, "transactions": transactions_result}

    def put(self, name: str):
        """Update an existing category"""
        existing_category = CategoryModel.query.get(name)
        if not existing_category:
            return {"msg": "Category not found."}, 404
        else:
            new_category = _category_schema.load(api.payload)
            existing_category.display_name = new_category.display_name
            db.session.commit()
            return _category_schema.dump(new_category)


class Transactions(Resource):
    def get(self):
        """Get all transactions"""
        transactions = TransactionModel.query.all()
        return _transactions_schema.dump(transactions)

    def post(self):
        """Create a new transaction"""
        new_transaction = _transaction_schema.load(api.payload)
        db.session.add(new_transaction)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            result = {
                "msg": "Tried to create a transaction with nonextant category",
                "data": _transaction_schema.dump(new_transaction),
            }
            return result, 400
        return _transaction_schema.dump(new_transaction), 201


class Transaction(Resource):
    def get(self, transaction_id: int):
        """Get a transaction by ID"""
        transaction = TransactionModel.query.get(transaction_id)
        if not transaction:
            return {"msg": f"Transaction not found with id: {transaction_id}"}, 404
        return _transaction_schema.dump(transaction)


api.add_resource(Category, "/categories/<name>")
api.add_resource(Categories, "/categories")
api.add_resource(Transaction, "/transactions/<transaction_id>")
api.add_resource(Transactions, "/transactions")
