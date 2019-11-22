from semantive.controller.main import db2


class Text(db2.Model):
    __tablename__ = 'text'
    id = db2.Column(db2.Integer, primary_key=True)
    url = db2.Column(db2.String(), nullable=False)
    text = db2.Column(db2.String(), nullable=True)

    def __init__(self, url, text):
        self.url = url
        self.text = text


class Image(db2.Model):
    __tablename__ = 'image'
    id = db2.Column(db2.Integer, primary_key=True)
    url = db2.Column(db2.String(), nullable=False)
    image = db2.Column(db2.String(), nullable=True)

    def __init__(self, url, image):
        self.url = url
        self.image = image
