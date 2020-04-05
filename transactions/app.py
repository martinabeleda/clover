from pathlib import Path
from typing import Optional

from flask import Flask, g
from flask_restful import Api
import markdown
from transactions.api import Categories, CategoryTypes, Transactions

app = Flask(__name__)

api = Api(app)


@app.teardown_appcontext
def teardown_db(exception: Optional[Exception]):
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.route("/")
def index():
    path = Path("/app/README.md")
    with path.open("r") as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


def main():
    app.run(host="0.0.0.0", port=80, debug=True)


api.add_resource(Categories, "/categories")
api.add_resource(CategoryTypes, "/category-types")
api.add_resource(Transactions, "/transactions")
