from pathlib import Path

from flask import Flask
from flask_restful import Api
import markdown
from transactions.api import Categories, CategoryTypes, Transactions

from .db import close_db

app = Flask(__name__)

api = Api(app)


@app.route("/")
def index():
    path = Path("/app/README.md")
    with path.open("r") as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


def main():
    app.teardown_appcontext(close_db)
    app.run(host="0.0.0.0", port=80, debug=True)


api.add_resource(Categories, "/categories")
api.add_resource(CategoryTypes, "/category-types")
api.add_resource(Transactions, "/transactions")
