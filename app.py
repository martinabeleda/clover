from transactions import api, create_app, db
from transactions.resources import Categories, Transactions


def main():
    config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config)
    db.create_all()
    api.add_resource(Categories, "/categories")
    api.add_resource(Transactions, "/transactions")
    app.run(debug=True)


if __name__ == "__main__":
    main()
