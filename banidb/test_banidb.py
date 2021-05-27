# -*- coding: utf-8 -*-
from unittest.mock import Mock, patch
import requests
import banidb.banidb


def backend_up():
    js = requests.get('https://api.banidb.com/v2/health').json()
    if js is True:
        return True
    else:
        return False


@patch('banidb.banidb.requests.get')
def test_backend_up(mock_get):
    mock_get.return_value.ok = True
    response = backend_up()
    assert response is False


def mock_search(query, searchtype=1, source='all', larivaar=False,
                ang=None, raag=None, writer='all', page=1, results=None):
    return banidb.search(query, searchtype, source, larivaar,
                         ang, raag, writer, page, results)


@patch('banidb.banidb.requests.get')
def test_search(mock_get):
    search_res = mock_search('nhknknkss')
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = search_res
    result = requests.get()
    assert result.json() == search_res
