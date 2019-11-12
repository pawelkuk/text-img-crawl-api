from flask_restful import Resource
from flask_restful import reqparse


class TaskStatus(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task-id',
                            type=int,
                            help='Task id has to be an int',
                            location='form')
        args = parser.parse_args()
        return {
            'task-id': args['task-id'],
            'status': 'RUNNING',
        }
