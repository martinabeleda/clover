from typing import Tuple

from flask_restful import Resource, fields, marshal_with
import pandas as pd

from .db import get_db

categories_fields = {"data": fields.Nested({"name": fields.String, "type": fields.String})}

category_types_fields = {"data": fields.Nested({"name": fields.String})}

transactions_fields = {
    "data": fields.Nested(
        {
            "time": fields.DateTime("iso8601"),
            "bsb_acc_num": fields.String(),
            "transaction_type": fields.String(),
            "payee": fields.String(),
            "description": fields.String(),
            "category": fields.String(""),
            "tags": fields.String(""),
            "subtotal": fields.String(),
            "currency": fields.String(),
            "subtotal_transaction_currency": fields.String(),
            "fee": fields.String(),
            "round_up": fields.String(),
            "total": fields.String(),
            "payment_method": fields.String(),
            "settled_date": fields.DateTime("iso8601"),
        }
    )
}


class Categories(Resource):
    @marshal_with(categories_fields)
    def get(self) -> Tuple[dict, int]:
        conn = get_db()
        sql = "SELECT * FROM categories"
        data = pd.read_sql(sql, conn).to_dict("records")
        return {"data": data}, 200


class CategoryTypes(Resource):
    @marshal_with(category_types_fields)
    def get(self) -> Tuple[dict, int]:
        conn = get_db()
        sql = "SELECT * FROM category_types"
        data = pd.read_sql(sql, conn).to_dict("records")
        return {"data": data}, 200


class Transactions(Resource):
    @marshal_with(transactions_fields)
    def get(self) -> Tuple[dict, int]:
        conn = get_db()
        sql = "SELECT * FROM transactions"
        data = pd.read_sql(sql, conn).to_dict("records")
        return {"data": data}, 200
