# -*- coding: utf-8 -*-
import requests
import json
import banidb
from requests_mock.mocker import Mocker

url = 'https://api.banidb.com/v2'


def test_backend_up(requests_mock: Mocker):
    back_url = f"{url}/health"
    result = {"ok": True}
    json_blob = json.loads(json.dumps(result))
    requests_mock.get(f"{back_url}", json=json_blob)

    def backend_up():
        js = requests.get('https://api.banidb.com/v2/health').json()
        if js['ok'] is True:
            return True
        else:
            return False
    result = backend_up()
    assert result is True


def test_shabad_ok_larivaar_false(requests_mock: Mocker):
    shabad_url = f"{url}/shabads/1111"
    result = {
        "shabadInfo": {
            "shabadId": 1111,
            "source": {
                "unicode": "source-unicode-ਸ੍ਰੀ",
                "english": "source-english",
                "pageNo": 111},
            "writer": {"english": "writer-english"}
            },

        "verses": [
                  {
                      "verseId": 11111,
                      "verse": {
                          "unicode": "verse-unicode-ਮਹਲਾ ॥"
                      },
                      "larivaar": {
                          "gurmukhi": "DnwsrImhlw5]",
                          "unicode": "ਧਨਾਸਰੀਮਹਲਾ੫॥"
                      },
                      "translation": {
                          "en": {
                              "bdb": "xlate-en-bdb",
                              "ms": "xlate-en-ms",
                              "ssk": "xlate-en-ssk"
                          },

                      },
                      "transliteration": {
                          "english": "transliteration-english",
                          "hindi": "transliteration-हिंदी",
                          "en": "transliteration-en",
                          "hi": "transliteration-हिं",
                          "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                          "ur": "دھن-transliteration"
                      },

                  }]
        }

    # convert dict to string to json
    json_blob = json.loads(json.dumps(result))
    requests_mock.get(f"{shabad_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.shabad(1111)

    assert result['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['source_eng'] == 'source-english'
    assert result['writer'] == 'writer-english'
    assert result['ang'] == 111
    assert result['verses'][0]['verse_id'] == 11111
    assert result['verses'][0]['verse'] == 'verse-unicode-ਮਹਲਾ ॥'
    assert result['verses'][0]['steek'] == {
        'en': {'bdb': 'xlate-en-bdb', 'ms': 'xlate-en-ms',
               'ssk': 'xlate-en-ssk'}}
    assert result['verses'][0]['transliteration'] == {
        "english": "transliteration-english",
        "hindi": "transliteration-हिंदी",
        "en": "transliteration-en",
        "hi": "transliteration-हिं",
        "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
        "ur": "دھن-transliteration"
    }
    assert 'larivaar' not in result['verses'][0]


def test_shabad_ok_larivaar_true(requests_mock: Mocker):
    shabad_url = f"{url}/shabads/1111"
    result = {
        "shabadInfo": {
            "shabadId": 1111,
            "source": {
                "unicode": "source-unicode-ਸ੍ਰੀ",
                "english": "source-english",
                "pageNo": 111},
            "writer": {"english": "writer-english"}
            },

        "verses": [
                  {
                      "verseId": 11111,
                      "verse": {
                          "unicode": "verse-unicode-ਮਹਲਾ ॥"
                      },
                      "larivaar": {
                          "gurmukhi": "DnwsrImhlw5]",
                          "unicode": "ਧਨਾਸਰੀਮਹਲਾ੫॥"
                      },
                      "translation": {
                          "en": {
                              "bdb": "xlate-en-bdb",
                              "ms": "xlate-en-ms",
                              "ssk": "xlate-en-ssk"
                          },

                      },
                      "transliteration": {
                          "english": "transliteration-english",
                          "hindi": "transliteration-हिंदी",
                          "en": "transliteration-en",
                          "hi": "transliteration-हिं",
                          "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                          "ur": "دھن-transliteration"
                      },

                  }]
        }

    # convert dict to string to json
    json_blob = json.loads(json.dumps(result))
    requests_mock.get(f"{shabad_url}", json=json_blob)
    result = banidb.shabad(1111, True)

    assert result['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['source_eng'] == 'source-english'
    assert result['writer'] == 'writer-english'
    assert result['ang'] == 111
    assert result['verses'][0]['verse_id'] == 11111
    assert result['verses'][0]['verse'] == "ਧਨਾਸਰੀਮਹਲਾ੫॥"  # for larivaar
    assert result['verses'][0]['steek'] == {
        'en': {'bdb': 'xlate-en-bdb', 'ms': 'xlate-en-ms',
               'ssk': 'xlate-en-ssk'}}
    assert result['verses'][0]['transliteration'] == {
        "english": "transliteration-english",
        "hindi": "transliteration-हिंदी",
        "en": "transliteration-en",
        "hi": "transliteration-हिं",
        "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
        "ur": "دھن-transliteration"
    }


def test_shabad_not_ok_larivaar_false(requests_mock: Mocker):
    result = banidb.shabad(1111)

    assert result['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['source_eng'] == 'source-english'
    assert result['writer'] != 'writer'
    assert result['ang'] == 111
    assert result['verses'][0]['verse_id'] == 11111
    assert result['verses'][0]['verse'] == 'verse-unicode-ਮਹਲਾ ॥'
    assert result['verses'][0]['steek'] != {
        'en': {'bdb': 'xlate-en-bdb'}}
    assert result['verses'][0]['transliteration'] == {
        "english": "transliteration-english",
        "hindi": "transliteration-हिंदी",
        "en": "transliteration-en",
        "hi": "transliteration-हिं",
        "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
        "ur": "دھن-transliteration"
    }
    assert 'larivaar' not in result['verses'][0]
