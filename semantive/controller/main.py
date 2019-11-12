from os.path import dirname
import markdown
from flask import Flask
from flask_restful import Api
from semantive.service.website_text_reader import WebsiteTextReader
from semantive.service.website_images_reader import WebsiteImageReader
from semantive.service.task_status import TaskStatus


app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    """Presents the readme file to the user."""
    with open(dirname(dirname(app.root_path)) + '/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)


api.add_resource(WebsiteTextReader, '/read-text')
api.add_resource(WebsiteImageReader, '/read-images')
api.add_resource(TaskStatus, '/status')
