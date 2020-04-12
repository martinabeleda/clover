from clover import create_app, db
from clover.resources import init_resources
from retrying import retry


def main():
    @retry(wait_exponential_multiplier=1000, wait_exponential_max=10000, stop_max_attempt_number=10)
    def create_tables():
        db.create_all()

    config = {
        "SQLALCHEMY_DATABASE_URI": "postgresql+psycopg2://db_user:db_password@db:5432",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False,
    }
    app = create_app(config)
    create_tables()
    init_resources()
    app.run(host="0.0.0.0", debug=True)


if __name__ == "__main__":
    main()
