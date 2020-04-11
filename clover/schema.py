from marshmallow import post_load
from clover import ma
from clover.models import CategoryModel, TransactionModel


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel

    @post_load
    def make_category(self, data, **kwargs):
        return CategoryModel(**data)


class TransactionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = TransactionModel
        include_fk = True

    @post_load
    def make_transaction(self, data, **kwargs):
        return TransactionModel(**data)
