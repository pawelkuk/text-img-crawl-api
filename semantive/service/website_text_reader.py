from flask_restful import Resource
from flask_restful import reqparse
import requests
import html2text


class WebsiteTextReader(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url',
                            type=str,
                            help='Input URL has to be a string',
                            location='form')
        args = parser.parse_args()
        page = requests.get(args['url'])

        h = html2text.HTML2Text()
        h.ignore_links = True

        text = h.handle(page.text).replace('\n', ' ').strip()
        return {"task-id": 1,
                "requested-url": args['url'],
                "text": text,
                }
