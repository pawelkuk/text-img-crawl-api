from flask_restful import Resource
from flask_restful import reqparse
from celery.result import AsyncResult


def add_resource_status(name, api, celery):
    class TaskStatus(Resource):
        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('task-id',
                                type=str,
                                help='Task id has to be a string',
                                location='form')
            args = parser.parse_args()
            result = AsyncResult(args['task-id'], app=celery)
            return {
                'task-id': args['task-id'],
                'status': result.status,
            }
    api.add_resource(TaskStatus, name)
