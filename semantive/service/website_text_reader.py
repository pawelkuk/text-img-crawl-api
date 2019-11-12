from flask_restful import Resource


class WebsiteTextReader(Resource):
    def get(self):
        return {
            "task-id": 1,
            "requested-url": "https://www.example.com",
            "text": "text content of the requested website without tags",
        }
