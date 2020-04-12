from clover import api, create_app, db
from clover.resources import Categories, Category, Transaction, Transactions
from retrying import retry


@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=10)
def create_tables():
    db.create_all()


def main():
    config = {
        "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg2://db_user:db_password@db:5432",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config)
    create_tables()
    api.add_resource(Category, "/categories/<name>")
    api.add_resource(Categories, "/categories")
    api.add_resource(Transaction, "/transactions/<transaction_id>")
    api.add_resource(Transactions, "/transactions")
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
