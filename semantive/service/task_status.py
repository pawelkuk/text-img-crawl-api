from flask_restful import Resource


class TaskStatus(Resource):
    def get(self):
        return {
            "task-id": 1,
            "status": "RUNNING",
        }
