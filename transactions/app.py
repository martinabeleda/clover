from pathlib import Path

from flask import Flask
import markdown

app = Flask(__name__)


@app.route("/")
def index():
    path = Path("/app/README.md")
    with path.open("r") as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)


def main():
    app.run(host="0.0.0.0", port=80, debug=True)
