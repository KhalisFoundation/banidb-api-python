# -*- coding: utf-8 -*-
from unittest.mock import Mock, patch
import requests
import banidb


@patch('banidb.banidb.requests.get')
def test_backend_up(mock_get):
    def backend_up():
        js = requests.get('https://api.banidb.com/v2/health').json()
        if js['ok'] is True:
            return True
        else:
            return False
    true = {'ok': True}
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = true
    response = backend_up()
    assert response is True


@patch('banidb.banidb.requests.get')
def test_search(mock_get):
    search_res = banidb.search('jmJdp')
    mock_get.return_value = Mock(ok=True)
    mock_get.return_value.json.return_value = search_res
    result = requests.get()
    assert result.json() == search_res
