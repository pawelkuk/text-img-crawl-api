from flask_restful import Resource
from flask_restful import reqparse
from bs4 import BeautifulSoup
import requests
import re
from .add_resources_text import save_data


def add_resources_image_reader(name, api, celery, db):
    """Func. which groups code associated with reading imgs from websites."""

    @celery.task(name='celery.get_images_and_save')
    def get_images_and_save(args):
        page = requests.get(args['url'])

        soup = BeautifulSoup(page.content, 'html.parser')
        images = soup.find_all('img', {'src': re.compile('.jpg')})
        images.extend(soup.find_all('img', {'src': re.compile('.png')}))

        image_src = []
        for image in images:
            image_src.append(image['src'])

        urls = src_to_urls(image_src, page.url)

        save_data(db, 'images', page.url, urls)

        return urls

    class WebsiteImageReader(Resource):
        """Class to be added to api's resources."""

        def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('url',
                                type=str,
                                help='Input URL has to be a string',
                                location='form')
            args = parser.parse_args()

            task = get_images_and_save.delay(args)
            return {
                'task-id': task.id,
                "requested-url": args['url'],
                }


def src_to_urls(image_src, url):
    """
    Given src values from html data converts it into valid urls.

    Keyword arguments:
    image_src -- list of src values of images
    url -- the url of page src values are comming from
    """
    urls = []
    protocol = 'https://'
    website = url.split('/')[2]
    for src in image_src:
        if '//' == src[0:2]:
            urls.append(''.join(['https:', src]))
            continue
        if 'http://' in src or 'https://' in src:
            urls.append(src)
            continue
        if website not in src:
            url = ''.join([protocol, website])
        url = ''.join([url, src])
        urls.append(url)

    return urls

    api.add_resource(WebsiteImageReader, name) # noqa
