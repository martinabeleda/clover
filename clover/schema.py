from marshmallow import post_load
from clover import ma
from clover.models import Category, Transaction


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
