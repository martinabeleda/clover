from clover import db


class Category(db.Model):
    __tablename__ = "categories"
    name = db.Column(db.String, primary_key=True, nullable=False)
    display_name = db.Column(db.String, unique=True, nullable=False)
    transactions = db.relationship("Transaction", backref="category", lazy=True)

    def __repr__(self):
        return f"Category(name={self.name}, display_name={self.display_name})"


class Transaction(db.Model):
    __tablename__ = "transactions"
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    transaction_type = db.Column(db.String)
    payee = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    total = db.Column(db.Float, nullable=False)
    category_name = db.Column(db.String, db.ForeignKey("categories.name"), nullable=False)

    def __repr__(self):
        return (
            f"Transaction("
            f"id={self.id}, "
            f"transaction_type={self.transaction_type}, "
            f"payee={self.payee}, "
            f"category_name={self.category_name}, "
            f"total={self.total})"
        )
