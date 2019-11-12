from os.path import dirname
import markdown
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Presents the readme file to the user."""
    with open(dirname(dirname(app.root_path)) + '/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)
