from flask_restful import Resource


class WebsiteImageReader(Resource):
    def get(self):
        return {
            "task-id": 1,
            "requested-url": "https://www.example.com",
            "images": [
                "img_1.jpeg",
                "img_2.jpeg", 
                "img_n.jpeg",
            ]
        }
