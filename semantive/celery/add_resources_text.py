from flask_restful import Resource
from flask_restful import reqparse
import requests
import html2text


def add_resource_text_reader(name, api, celery, db):

    @celery.task(name='celery.get_text_and_save')
    def get_text_and_save(args):
        page = requests.get(args['url'])
        h = html2text.HTML2Text()
        h.ignore_links = True
        text = h.handle(page.text).replace('\n', ' ').strip()

        save_data(db, 'text', page.url, text)

        return text

    class WebsiteTextReader(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('url',
                                type=str,
                                help='Input URL has to be a string',
                                location='form')
            args = parser.parse_args()

            task = get_text_and_save.delay(args)

            return {"task-id": task.id, }
    api.add_resource(WebsiteTextReader, name)


def save_data(db, dict_key, url, data_to_store):
    if dict_key not in db:
        db[dict_key] = []
    data = db[dict_key]
    data.append({
        'url': url,
        'data': data_to_store,
    })
    db[dict_key] = data