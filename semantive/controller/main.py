from os.path import dirname
import markdown
from flask import Flask
from flask_restful import Api
from semantive.service.website_text_reader import WebsiteTextReader
from semantive.service.website_images_reader import WebsiteImageReader
from semantive.service.task_status import TaskStatus
from semantive.celery.celery_flask import make_celery


app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://redis:6379',
    CELERY_RESULT_BACKEND='redis://redis:6379'
)
api = Api(app)
celery = make_celery(app)


@app.route('/')
def index():
    """Presents the readme file to the user."""
    with open(dirname(dirname(app.root_path)) + '/README.md', 'r') as file:
        content = file.read()
        return markdown.markdown(content)


@app.route('/process/<name>')
def process(name):
    reverse.delay(name)
    return 'I sent an async request!'


@celery.task(name='celery_example.reverse')
def reverse(string):
    return string[::-1]


api.add_resource(WebsiteTextReader, '/read-text')
api.add_resource(WebsiteImageReader, '/read-images')
api.add_resource(TaskStatus, '/status')
