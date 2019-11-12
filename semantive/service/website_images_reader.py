from flask_restful import Resource
from flask_restful import reqparse
from bs4 import BeautifulSoup
import requests
import re


class WebsiteImageReader(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url',
                            type=str,
                            help='Input URL has to be a string',
                            location='form')
        args = parser.parse_args()
        page = requests.get(args['url'])

        soup = BeautifulSoup(page.content, 'html.parser')
        images = soup.find_all('img', {'src': re.compile('.jpg')})
        images.extend(soup.find_all('img', {'src': re.compile('.png')}))

        image_src = []
        for image in images:
            image_src.append(image['src'])

        urls = src_to_urls(image_src, page)

        return {"task-id": 1,
                "requested-url": args['url'],
                "images": urls,
                "images_2": image_src,
                }


def src_to_urls(image_src, page):
    urls = []
    protocol = 'https://'
    website = page.url.split('/')[2]
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
