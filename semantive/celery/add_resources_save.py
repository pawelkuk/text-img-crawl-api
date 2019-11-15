from flask_restful import Resource
from flask_restful import reqparse
import csv


def add_resource_save(name, api, celery, db):
    """Function which groups code associated with saving data."""

    @celery.task(name='celery.save')
    def save(args):
        if args['content'] not in ['text', 'images']:
            return {'STATUS': 'FAILURE', }

        data = extract_data(args['content'], db)

        with open('data.csv', "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',', quotechar='`')
            for line in data:
                writer.writerow(line)
        return {
            'STATUS': 'SUCCESS',
            'file-name': 'data.csv',
            }

    class SaveContent(Resource):
        """Class to be added to api's resources."""

        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('content',
                                type=str,
                                help='Input type has to be a string',
                                location='form')
            args = parser.parse_args()
            task = save.delay(args)

            return {
                "task-id": task.id,
                'requested-content': args['content']
                }
    api.add_resource(SaveContent, name)


def extract_data(content_type, db):
    data = []
    if content_type not in db.keys():
        return data
    if content_type == 'images':
        img_dict = db['images']
        for site in img_dict:
            for image in site['data']:
                data.append([site['url'], image])

    elif content_type == 'text':
        text_dict = db['text']
        for line in text_dict:
            data.append([line['url'], line['data']])
    return data
