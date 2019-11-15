from os.path import dirname
import markdown
from flask import Flask
from flask import g
import shelve
from flask_restful import Api
from werkzeug.local import LocalProxy
from semantive.celery.celery_flask import make_celery
from semantive.celery.add_resources_text import add_resource_text_reader
from semantive.celery.add_resources_images import add_resources_image_reader
from semantive.service.add_resources_status import add_resource_status
from semantive.celery.add_resources_save import add_resource_save

app = Flask(__name__)
app.config.update(
    CELERY_BROKER_URL='redis://redis:6379',
    CELERY_RESULT_BACKEND='redis://redis:6379'
)
api = Api(app)
celery = make_celery(app)


def get_db():
    if 'db' not in g:
        g.db = shelve.open('data.db')

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


db = LocalProxy(get_db)


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


add_resource_text_reader('/read-text', api, celery, db)
add_resources_image_reader('/read-images', api, celery, db)
add_resource_status('/status', api, celery)
add_resource_save('/save', api, celery, db)
