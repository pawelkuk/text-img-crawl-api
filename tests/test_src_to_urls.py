import pytest
from semantive.celery.add_resources_images import src_to_urls


def test_src_to_urls_handles_empty_list():
    src = []
    url = 'https://www.example.com'
    assert src_to_urls(src, url) == []


def test_src_to_urls_handles_valid_urls():
    url = 'https://www.example.com'
    src = [url+"/1", url+'/2']
    assert src_to_urls(src, url) == src


def test_src_to_urls_handles_input_starting_with_slash():
    url = 'https://www.example.com'
    src = '//www.example.com'
    src_list = [src+"/1", src+'/2']
    assert src_to_urls(src_list, url) == [url+"/1", url+'/2']
