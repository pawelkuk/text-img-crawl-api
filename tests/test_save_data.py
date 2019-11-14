import pytest
from semantive.celery.add_resources_text import save_data
import shelve


def test_save_data_empty_db_returns_proper_structure_for_text_data(tmp_path):
    file_ = tmp_path / "shelve"
    db = shelve.open(str(file_))
    data_to_store = 'some str'
    key = 'text'
    url = 'https://www.example.com'
    save_data(db, key, url, data_to_store)
    assert key in db
    assert type(db[key]) == list
    data = db[key]
    assert len(data) == 1
    data_dict = data[0]
    assert data_dict['url'] == url
    assert data_dict['data'] == data_to_store


def test_save_data_empty_db_returns_proper_structure_for_list_data(tmp_path):
    file_ = tmp_path / "shelve"
    db = shelve.open(str(file_))
    url = 'https://www.example.com'
    data_to_store = [url+'/1', url+'/2']
    key = 'text'
    save_data(db, key, url, data_to_store)
    assert key in db
    assert type(db[key]) == list
    data = db[key]
    assert len(data) == 1
    data_dict = data[0]
    assert data_dict['url'] == url
    assert type(data_dict['data']) == list
    assert len(data_dict['data']) == len(data_to_store)
