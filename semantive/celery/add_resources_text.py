from flask_restful import Resource
from flask_restful import reqparse
import requests
import html2text


def add_resource_text_reader(name, api, celery, db):
    """Func. which groups code associated with reading text from websites."""

    @celery.task(name='celery.get_text_and_save')
    def get_text_and_save(args):
        page = requests.get(args['url'])
        h = html2text.HTML2Text()
        h.ignore_links = True
        text = h.handle(page.text).replace('\n', ' ').strip()

        save_data(db, 'text', page.url, text)

        return text

    class WebsiteTextReader(Resource):
        """Class to be added to api's resources."""
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('url',
                                type=str,
                                help='Input URL has to be a string',
                                location='form')
            args = parser.parse_args()

            task = get_text_and_save.delay(args)

            return {
                "task-id": task.id,
                "requested-url": args['url'],
                }
    api.add_resource(WebsiteTextReader, name)


def save_data(db, dict_key, url, data_to_store):
    """
    Given url and data stores it in a shelve object.

    Keyword arguments:
    db -- shelve object
    dict_key -- the key data has to be append under
    url -- for keeping track from what website is the data comming from
    data_to_store -- has to be serializable (potential security issue
    because shelve uses the pickle module)
    """
    if dict_key not in db:
        db[dict_key] = []
    data = db[dict_key]
    data.append({
        'url': url,
        'data': data_to_store,
    })
    db[dict_key] = data
