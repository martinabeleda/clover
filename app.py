from clover import api, create_app, db
from clover.resources import Categories, Transactions


def main():
    config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///test.db",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config)
    db.create_all()
    api.add_resource(Categories, "/categories")
    api.add_resource(Transactions, "/transactions")
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
