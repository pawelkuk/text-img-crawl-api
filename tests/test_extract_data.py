from semantive.celery.add_resources_save import extract_data
import shelve


def test_extract_data_empty_db(tmp_path):
    file_ = tmp_path / "shelve"
    db = shelve.open(str(file_))
    assert extract_data('text', db) == []
    assert extract_data('images', db) == []


def test_extract_data_populated_db(tmp_path):
    file_ = tmp_path / "shelve"
    db = shelve.open(str(file_))
    url = 'https://www.example.com'
    db['text'] = [{
        'url': url,
        'data': 'some data',
    }, ]
    db['images'] = [{
        'url': url,
        'data': [url+'/1', url+'/2', ],
    }, ]
    extracted_text_data = [[url, 'some data', ], ]
    extracted_image_data = [
        [url, url+'/1', ],
        [url, url+'/2', ]
        ]
    assert extract_data('text', db)[0] == extracted_text_data[0]
    assert extract_data('images', db)[0] == extracted_image_data[0]
    assert extract_data('images', db)[1] == extracted_image_data[1]
