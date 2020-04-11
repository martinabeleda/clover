from flask_restx import Resource
from sqlalchemy.exc import IntegrityError
from clover import api, db
from clover.models import Category, Transaction
from clover.schema import CategorySchema, TransactionSchema


class Categories(Resource):
    def get(self):
        categories = Category.query.all()
        return CategorySchema(many=True).dump(categories)

    def post(self):
        category_schema = CategorySchema()
        new_category = category_schema.load(api.payload)
        db.session.add(new_category)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            existing_category = Category.query.get(new_category.name)
            return {"msg": "Category already exists", "data": category_schema.dump(existing_category)}, 409
        else:
            return category_schema.dump(new_category), 201


class Transactions(Resource):
    def get(self):
        transactions = Transaction.query.all()
        return TransactionSchema(many=True).dump(transactions)

    def post(self):
        transaction_schema = TransactionSchema()
        new_transaction = transaction_schema.load(api.payload)
        db.session.add(new_transaction)
        db.session.commit()
        return transaction_schema.dump(new_transaction), 201