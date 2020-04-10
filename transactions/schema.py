from marshmallow import post_load
from transactions import ma
from transactions.models import Category, Transaction


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category

    @post_load
    def make_category(self, data, **kwargs):
        return Category(**data)


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Transaction
        include_fk = True

    @post_load
    def make_transaction(self, data, **kwargs):
        return Transaction(**data)
