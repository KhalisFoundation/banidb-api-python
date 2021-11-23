# -*- coding: utf-8 -*-
from banidb.banidb import amritkeertan_shabad
import json

import pytest
import requests
from requests_mock.mocker import Mocker

import banidb

url = 'https://api.banidb.com/v2'


@pytest.fixture
def clear_cache():
    banidb.clear()


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


def get_search_json_blob():
    search_url = f"{url}/search/bhbgggr"
    result = {
        "resultsInfo": {
            "totalResults":1,
            "pageResults":1,
            "pages":{
                "page":1,
                "resultsPerPage":20,
                "totalPages":1
                }
        },
        "verses":[
            {
                "verseId":11111,
                "shabadId":1111,
                "verse": {
                    "gurmukhi":"verse-gurmukhi",
                    "unicode":"verse-unicode"
                },
                "larivaar": {
                    "gurmukhi": "lari-gurmukhi]",
                    "unicode": "lari-unicode"
                },
                "translation":{
                    "en": {
                        "bdb": "xlate-en-bdb",
                        "ms": "xlate-en-ms",
                        "ssk": "xlate-en-ssk"
                    },
                    "pu": {
                        "bdb": {
                            "gurmukhi" :"xlate-pu-bdb-gur",
                            "unicode" : "xlate-pu-bdb-uni"
                        },
                        "ms": "xlate-pu-ms",
                        "ssk": "xlate-pu-ssk"
                    }
                },
                "transliteration":{
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                },
                "pageNo":111,
                "lineNo":11,
                "writer":{
                    "writerId":1,
                    "gurmukhi":"writer-gurmukhi",
                    "english": "writer-english"
                },
                "source":{
                    "sourceId":"G",
                    "gurmukhi":"source-gurmukhi",
                    "unicode":"source-unicode",
                    "english": "source-english",
                    "pageNo":111
                },
                "raag":{
                    "raagId":11,
                    "gurmukhi":"raag-gurmukhi",
                    "unicode":"raag-unicode",
                    "english":"raag-english",
                    "raagWithPage":"raag(pages)"
                }
            }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, search_url


def test_search_ok_larivaar_false(clear_cache, requests_mock: Mocker):
    json_blob, search_url = get_search_json_blob()

    requests_mock.get(f"{search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.search('bhbgggr')
    print(result)

    assert result['pages_data']['page_1'][0]['source']['pu'] == 'source-unicode'
    assert result['pages_data']['page_1'][0]['source']['en']  == 'source-english'
    assert result['pages_data']['page_1'][0]['source']['writer'] == 'writer-english'
    assert result['pages_data']['page_1'][0]['source']['ang'] == 111
    assert result['pages_data']['page_1'][0]['verse'] == "verse-unicode"
    assert result['pages_data']['page_1'][0]['steek'] == {
        'en': 'xlate-en-bdb', 'pu': 'xlate-pu-bdb-uni'}
    assert result['pages_data']['page_1'][0]['source']['raagpu'] == 'raag-unicode'
    assert result['pages_data']['page_1'][0]['source']['raagen'] == 'raag-english'
    assert 'lari' not in result['pages_data']['page_1'][0]

def test_search_ok_larivaar_true(clear_cache, requests_mock: Mocker):
    json_blob, search_url = get_search_json_blob()

    requests_mock.get(f"{search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.search('bhbgggr', larivaar=True)
    print(result)

    assert 'lari' in result['pages_data']['page_1'][0]
    assert result['pages_data']['page_1'][0]['source']['pu'] == 'source-unicode'
    assert result['pages_data']['page_1'][0]['source']['en']  == 'source-english'
    assert result['pages_data']['page_1'][0]['source']['writer'] == 'writer-english'
    assert result['pages_data']['page_1'][0]['source']['ang'] == 111
    assert result['pages_data']['page_1'][0]['lari'] == "lari-unicode" # for larivaar
    assert result['pages_data']['page_1'][0]['steek'] == {
        'en': 'xlate-en-bdb', 'pu': 'xlate-pu-bdb-uni'}
    assert result['pages_data']['page_1'][0]['source']['raagpu'] == 'raag-unicode'
    assert result['pages_data']['page_1'][0]['source']['raagen'] == 'raag-english'

def test_search_not_ok_larivaar_false(clear_cache, requests_mock: Mocker):
    json_blob, search_url = get_search_json_blob()

    requests_mock.get(f"{search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.search('bhbgggr')
    print(result)

    assert result['pages_data']['page_1'][0]['source']['pu'] == 'source-unicode'
    assert result['pages_data']['page_1'][0]['source']['en']  == 'source-english'
    assert result['pages_data']['page_1'][0]['source']['writer'] != 'writer'
    assert result['pages_data']['page_1'][0]['source']['ang'] == 111
    assert result['pages_data']['page_1'][0]['verse'] == "verse-unicode"
    assert result['pages_data']['page_1'][0]['steek'] == {
        'en': 'xlate-en-bdb', 'pu': 'xlate-pu-bdb-uni'}
    assert result['pages_data']['page_1'][0]['source']['raagpu'] == 'raag-unicode'
    assert result['pages_data']['page_1'][0]['source']['raagen'] == 'raag-english'
    assert 'lari' not in result['pages_data']['page_1'][0]


def get_shabad_json_blob():
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
    return json_blob, shabad_url


def test_shabad_ok_larivaar_false(clear_cache, requests_mock: Mocker):

    json_blob, shabad_url = get_shabad_json_blob()

    requests_mock.get(f"{shabad_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.shabad(1111)
    print(result)

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


def test_shabad_ok_larivaar_true(clear_cache, requests_mock: Mocker):
    json_blob, shabad_url = get_shabad_json_blob()

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


def test_shabad_not_ok_larivaar_false(clear_cache, requests_mock: Mocker):
    json_blob, shabad_url = get_shabad_json_blob()
    requests_mock.get(f"{shabad_url}", json=json_blob)

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




def get_ang_json_blob():
    ang_url = f"{url}/angs/1/G"
    result = {
              "source": {
                "sourceId": "G",
                "gurmukhi": "source-gurmukhi",
                "unicode": "source-unicode",
                "english": "source-english",
                "pageNo": 1
              },
              "count": 23,
              "page": [
                {
                  "verseId": 1,
                  "shabadId": 1,
                  "verse": {
                    "gurmukhi":"verse-gurmukhi",
                    "unicode":"verse-unicode"
                },
                "larivaar": {
                    "gurmukhi": "lari-gurmukhi",
                    "unicode": "lari-unicode"
                },
                "translation":{
                    "en": {
                        "bdb": "xlate-en-bdb",
                        "ms": "xlate-en-ms",
                        "ssk": "xlate-en-ssk"
                    },
                    "pu": {
                        "bdb": {
                            "gurmukhi" :"xlate-pu-bdb-gur",
                            "unicode" : "xlate-pu-bdb-uni"
                        },
                        "ms": "xlate-pu-ms",
                        "ssk": "xlate-pu-ssk"
                    }
                },
                "transliteration":{
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                },
                "pageNo": 1,
                "lineNo": 1,
                "writer": {
                    "writerId":1,
                    "gurmukhi":"writer-gurmukhi",
                    "english": "writer-english"
                  },
                  "raag": {
                    "raagId": 1,
                    "gurmukhi":"raag-gurmukhi",
                    "unicode":"raag-unicode",
                    "english":"raag-english",
                    "raagWithPage":"raag(pages)"
                  }
            }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, ang_url


def test_ang_ok_larivaar_false_steek_false_translit_false(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1)
    print(result)

    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1
    assert result['page'][0]['verse'] == 'verse-unicode'


def test_ang_ok_larivaar_true_steek_false_translit_false(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1, larivaar=True)
    print(result)

    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1
    assert result['page'][0]['verse'] == 'lari-unicode'

def test_ang_ok_larivaar_false_steek_true_translit_false(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1, steek=True)
    print(result)

    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1
    assert result['page'][0]['verse'] == 'verse-unicode'
    assert result['page'][0]['steek'] == {
        "en": {
            "bdb": "xlate-en-bdb",
            "ms": "xlate-en-ms",
            "ssk": "xlate-en-ssk"
        },
        "pu": {
            "bdb": {
                "gurmukhi" :"xlate-pu-bdb-gur",
                "unicode" : "xlate-pu-bdb-uni"
            },
            "ms": "xlate-pu-ms",
            "ssk": "xlate-pu-ssk"
        }
    }


def test_ang_ok_larivaar_false_steek_false_translit_true(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1, translit=True)
    print(result)

    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1
    assert result['page'][0]['verse'] == 'verse-unicode'
    assert result['page'][0]['translit'] == {
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                }


def test_ang_ok_larivaar_true_steek_true_translit_true(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1, larivaar=True, steek=True, translit=True)
    print(result)

    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1
    assert result['page'][0]['verse'] == 'lari-unicode'
    assert result['page'][0]['steek'] == {
        "en": {
            "bdb": "xlate-en-bdb",
            "ms": "xlate-en-ms",
            "ssk": "xlate-en-ssk"
        },
        "pu": {
            "bdb": {
                "gurmukhi" :"xlate-pu-bdb-gur",
                "unicode" : "xlate-pu-bdb-uni"
            },
            "ms": "xlate-pu-ms",
            "ssk": "xlate-pu-ssk"
        }
    }
    assert result['page'][0]['translit'] == {
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                }


def test_ang_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, ang_url = get_ang_json_blob()

    requests_mock.get(f"{ang_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.angs(1)
    print(result)

    assert result['page'][0]['verse'] != 'lari-unicode'
    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['source']['ang_no'] == 1


def get_hukamnama_json_blob():
    hukam_url = f"{url}/hukamnamas/2010/10/10"
    result = {'shabads': [{'shabadInfo': {'shabadId': 1111}}]}
    json_blob = json.loads(json.dumps(result))
    return json_blob, hukam_url


def test_hukamnama_ok(clear_cache, requests_mock: Mocker):
    # preparing backend shabad
    shabad_blob, shabad_url = get_shabad_json_blob()
    requests_mock.get(f"{shabad_url}", json=shabad_blob)

    # getting random data
    json_blob, hukam_url = get_hukamnama_json_blob()
    requests_mock.get(f"{hukam_url}", json=json_blob)

    result = banidb.hukamnama(2010, 10, 10)
    print(result)

    assert result['hukam'][0]['shabad_id'] == 1111
    assert result['hukam'][0]['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['hukam'][0]['source_eng'] == 'source-english'
    assert result['hukam'][0]['writer'] == 'writer-english'
    assert result['hukam'][0]['ang'] == 111
    assert result['hukam'][0]['verses'][0]['verse_id'] == 11111
    assert result['hukam'][0]['verses'][0]['verse'] == 'verse-unicode-ਮਹਲਾ ॥'
    assert result['hukam'][0]['verses'][0]['steek'] == {
        'en': {'bdb': 'xlate-en-bdb', 'ms': 'xlate-en-ms',
               'ssk': 'xlate-en-ssk'}}
    assert result['hukam'][0]['verses'][0]['transliteration'] == {
        "english": "transliteration-english",
        "hindi": "transliteration-हिंदी",
        "en": "transliteration-en",
        "hi": "transliteration-हिं",
        "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
        "ur": "دھن-transliteration"
    }
    assert 'larivaar' not in result['hukam'][0]['verses'][0]


def test_hukamnama_not_ok(clear_cache, requests_mock: Mocker):
    # preparing backend shabad
    shabad_blob, shabad_url = get_shabad_json_blob()
    requests_mock.get(f"{shabad_url}", json=shabad_blob)

    # getting random data
    json_blob, hukam_url = get_hukamnama_json_blob()
    requests_mock.get(f"{hukam_url}", json=json_blob)

    result = banidb.hukamnama(2010, 10, 10)
    print(result)
    
    assert result['hukam'][0]['shabad_id'] == 1111
    assert result['hukam'][0]['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['hukam'][0]['source_eng'] != 'source'
    assert result['hukam'][0]['writer'] == 'writer-english'
    assert result['hukam'][0]['ang'] == 111
    assert result['hukam'][0]['verses'][0]['verse_id'] == 11111
    assert result['hukam'][0]['verses'][0]['verse'] != 'verse-uni'
    assert 'larivaar' not in result['hukam'][0]['verses'][0]




def get_random_json_blob():
    random_url = f"{url}/random/G"
    result = {'shabadInfo': {'shabadId': 1111}}
    json_blob = json.loads(json.dumps(result))
    return json_blob, random_url

def test_random_ok(clear_cache, requests_mock: Mocker):
    # getting random data
    json_blob, random_url = get_random_json_blob()
    requests_mock.get(f"{random_url}", json=json_blob)

    # preparing backend shabad
    shabad_blob, shabad_url = get_shabad_json_blob()
    requests_mock.get(f"{shabad_url}", json=shabad_blob)

    result = banidb.random()
    
    assert result['shabad_id'] == 1111
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


def test_random_not_ok(clear_cache, requests_mock: Mocker):
    # getting random data
    json_blob, random_url = get_random_json_blob()
    requests_mock.get(f"{random_url}", json=json_blob)

    # preparing backend shabad
    shabad_blob, shabad_url = get_shabad_json_blob()
    requests_mock.get(f"{shabad_url}", json=shabad_blob)

    result = banidb.random()
    
    assert result['shabad_id'] == 1111
    assert result['source_uni'] == 'source-unicode-ਸ੍ਰੀ'
    assert result['source_eng'] != 'source'
    assert result['writer'] == 'writer-english'
    assert result['ang'] == 111
    assert result['verses'][0]['verse_id'] == 11111
    assert result['verses'][0]['verse'] != 'verse-uni'
    assert 'larivaar' not in result['verses'][0]


def get_banis_json_blob():
    banis_url = f"{url}/banis"
    result = [{
        "ID":1,
        "token":"token",
        "gurmukhiUni":"bani-uni",
        "transliteration":"translit",
        "transliterations":{
            "english": "transliteration-english",
            "hindi": "transliteration-हिंदी",
            "en": "transliteration-en",
            "hi": "transliteration-हिं",
            "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
            "ur": "دھن-transliteration"
        }
    }]
    json_blob = json.loads(json.dumps(result))
    return json_blob, banis_url

def test_banis_ok(clear_cache, requests_mock: Mocker):
    json_blob, banis_url = get_banis_json_blob()

    requests_mock.get(f"{banis_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.banis()
    print(result)

    assert result[1]['gurmukhiUni'] == "bani-uni"
    assert result[1]['transliterations'] == {
            "english": "transliteration-english",
            "hindi": "transliteration-हिंदी",
            "en": "transliteration-en",
            "hi": "transliteration-हिं",
            "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
            "ur": "دھن-transliteration"
        }

def test_banis_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, banis_url = get_banis_json_blob()

    requests_mock.get(f"{banis_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.banis()
    print(result)

    assert result[1]['gurmukhiUni'] != "bani"
    assert result[1]['transliterations'] == {
            "english": "transliteration-english",
            "hindi": "transliteration-हिंदी",
            "en": "transliteration-en",
            "hi": "transliteration-हिं",
            "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
            "ur": "دھن-transliteration"
        }


def get_bani_json_blob():
    bani_url = f"{url}/banis/1"
    result = {
        "baniInfo": {
            "baniID": 1,
            "gurmukhi": "bani-gurmukhi",
            "unicode": "bani-uni",
            "english": "bani-english",
            "hindi": "bani-hindi",
            "ipa": "bani-ipa",
            "ur": "bani-ur",
            "source": {
                "sourceId": "G",
                "gurmukhi": "source-gurmukhi",
                "unicode": "source-unicode",
                "english": "source-english",
                "pageNo": 1
            },
            "raag": {
                "raagId": 1,
                "gurmukhi":"raag-gurmukhi",
                "unicode":"raag-unicode",
                "english":"raag-english",
                "raagWithPage":"raag(pages)"
            },
            "writer": {
                "writerId":1,
                "gurmukhi":"writer-gurmukhi",
                "english": "writer-english"
            }
          },
          "verses": [
            {
              "verse": {
                "verseId": 1,
                "verse": {
                    "gurmukhi":"verse-gurmukhi",
                    "unicode":"verse-unicode"
                },
                "larivaar": {
                    "gurmukhi": "lari-gurmukhi",
                    "unicode": "lari-unicode"
                },
                "translation": {
                    "en": {
                        "bdb": "xlate-en-bdb",
                        "ms": "xlate-en-ms",
                        "ssk": "xlate-en-ssk"
                    },
                    "pu": {
                        "bdb": {
                            "gurmukhi" :"xlate-pu-bdb-gur",
                            "unicode" : "xlate-pu-bdb-uni"
                        },
                        "ms": "xlate-pu-ms",
                        "ssk": "xlate-pu-ssk"
                    }
                },
                "transliteration": {
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                },
                "pageNo": 1,
                "lineNo": 1,
              }
            }]
        }
    json_blob = json.loads(json.dumps(result))
    return json_blob, bani_url


def test_bani_ok_larivaar_false(clear_cache, requests_mock: Mocker):
    json_blob, bani_url = get_bani_json_blob()
    requests_mock.get(f"{bani_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.bani(1)
    print(result)

    assert result['info']['bani_id'] == 1
    assert result['info']['unicode'] == 'bani-uni'
    assert result['info']['english'] == 'bani-english'
    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['verses'][0]['verse'] == 'verse-unicode'
    assert result['verses'][0]['steek'] == {
        "en": {
            "bdb": "xlate-en-bdb",
            "ms": "xlate-en-ms",
            "ssk": "xlate-en-ssk"
        },
        "pu": {
            "bdb": {
                "gurmukhi" :"xlate-pu-bdb-gur",
                "unicode" : "xlate-pu-bdb-uni"
            },
            "ms": "xlate-pu-ms",
            "ssk": "xlate-pu-ssk"
        }
    }
    assert result['verses'][0]['translit'] == {
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                }


def test_bani_ok_larivaar_true(clear_cache, requests_mock: Mocker):
    json_blob, bani_url = get_bani_json_blob()
    requests_mock.get(f"{bani_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.bani(1,larivaar=True)
    print(result)

    assert result['info']['bani_id'] == 1
    assert result['info']['unicode'] == 'bani-uni'
    assert result['info']['english'] == 'bani-english'
    assert result['source']['unicode'] == 'source-unicode'
    assert result['source']['english'] == 'source-english'
    assert result['verses'][0]['verse'] == 'lari-unicode'
    assert result['verses'][0]['steek'] == {
        "en": {
            "bdb": "xlate-en-bdb",
            "ms": "xlate-en-ms",
            "ssk": "xlate-en-ssk"
        },
        "pu": {
            "bdb": {
                "gurmukhi" :"xlate-pu-bdb-gur",
                "unicode" : "xlate-pu-bdb-uni"
            },
            "ms": "xlate-pu-ms",
            "ssk": "xlate-pu-ssk"
        }
    }
    assert result['verses'][0]['translit'] == {
                    "english": "transliteration-english",
                    "hindi": "transliteration-हिंदी",
                    "en": "transliteration-en",
                    "hi": "transliteration-हिं",
                    "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                    "ur": "دھن-transliteration"
                }


def test_bani_not_ok_larivaar_false(clear_cache, requests_mock: Mocker):
    json_blob, bani_url = get_bani_json_blob()
    requests_mock.get(f"{bani_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.bani(1)
    print(result)

    assert result['info']['bani_id'] == 1
    assert result['info']['unicode'] != 'bani'
    assert result['info']['english'] == 'bani-english'
    assert result['source']['unicode'] != 'source'
    assert result['source']['english'] == 'source-english'
    assert result['verses'][0]['verse'] != 'verse'


def get_amritkeertan_json_blob():
    ak_url = f"{url}/amritkeertan"
    result = {
        "headers": [{
            "HeaderID": 1,
            "Gurmukhi": "head-gurmukhi",
            "GurmukhiUni": "head-uni",
            "Transliterations": {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, ak_url


def test_amritkeertan_ok(clear_cache, requests_mock: Mocker):
    json_blob, ak_url = get_amritkeertan_json_blob()
    requests_mock.get(f"{ak_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan()
    print(result)

    assert result[0]['header_id'] == 1
    assert result[0]['gurmukhi'] == 'head-gurmukhi'
    assert result[0]['gurmukhi_uni'] == 'head-uni'
    assert result[0]['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }


def test_amritkeertan_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, ak_url = get_amritkeertan_json_blob()
    requests_mock.get(f"{ak_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan()
    print(result)

    assert result[0]['header_id'] == 1
    assert result[0]['gurmukhi'] != 'head'
    assert result[0]['gurmukhi_uni'] != 'head'
    assert result[0]['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }


def get_akindex_json_blob():
    akindex_url = f"{url}/amritkeertan/index"
    result = {
        "index":[{
            "IndexID":1,
            "HeaderID":1,
            "ShabadID":111,
            "PageNo":1,
            "Gurmukhi":"index-gurmukhi",
            "GurmukhiUni":"index-uni",
            "Translations":{
                "en": {
                    "bdb": "xlate-en-bdb",
                    "ms": "xlate-en-ms",
                    "ssk": "xlate-en-ssk"
                },
                "pu": {
                    "bdb": {
                        "gurmukhi" :"xlate-pu-bdb-gur",
                        "unicode" : "xlate-pu-bdb-uni"
                    },
                    "ms": "xlate-pu-ms",
                    "ssk": "xlate-pu-ssk"
                }
            },
            "Ang":111,
            "LineNo":1,
            "SourceID":"G",
            "Transliterations":{
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            },
            "WriterID":1,
            "WriterEnglish":"writer-english",
            "WriterGurmukhi":"writer-gurmukhi",
            "RaagID":1,
            "RaagGurmukhi":"raag-gurmukhi",
            "RaagUnicode":"raag-uni",
            "RaagEnglish":"raag-english",
            "RaagWithPage":"raag(pages)",
            "SourceGurmukhi":"source-gurmukhi",
            "SourceUnicode":"source-uni",
            "SourceEnglish":"source-eng"
            }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, akindex_url


def test_akindex_ok(clear_cache, requests_mock: Mocker):
    json_blob, akindex_url = get_akindex_json_blob()
    requests_mock.get(f"{akindex_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan_index()
    print(result)

    assert result[0]['index_id'] == 1
    assert result[0]['gurmukhi_uni'] == 'index-uni'
    assert result[0]['steek'] == {
                "en": {
                    "bdb": "xlate-en-bdb",
                    "ms": "xlate-en-ms",
                    "ssk": "xlate-en-ssk"
                },
                "pu": {
                    "bdb": {
                        "gurmukhi" :"xlate-pu-bdb-gur",
                        "unicode" : "xlate-pu-bdb-uni"
                    },
                    "ms": "xlate-pu-ms",
                    "ssk": "xlate-pu-ssk"
                }
            }
    assert result[0]['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }
    assert result[0]['source_id'] == 'G'
    assert result[0]['writer'] == 'writer-english'


def test_akindex_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, akindex_url = get_akindex_json_blob()
    requests_mock.get(f"{akindex_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan_index()
    print(result)

    assert result[0]['index_id'] == 1
    assert result[0]['gurmukhi_uni'] != 'index'
    assert result[0]['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }
    assert result[0]['writer'] != 'writer'


def get_aksearch_json_blob():
    aksearch_url = f"{url}/amritkeertan/index/1"
    result = {
        "header":[{
            "HeaderID":1,
            "Gurmukhi":"head-gurmukhi",
            "GurmukhiUni":"head-uni",
            "Transliterations":{
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            },
        }],
        "index":[{
            "IndexID":11,
            "HeaderID":1,
            "ShabadID":1111,
            "PageNo":111,
            "Gurmukhi":"index-gurmukhi",
            "GurmukhiUni":"index-uni",
            "Translations":{
                "en": {
                    "bdb": "xlate-en-bdb",
                    "ms": "xlate-en-ms",
                    "ssk": "xlate-en-ssk"
                },
                "pu": {
                    "bdb": {
                        "gurmukhi" :"xlate-pu-bdb-gur",
                        "unicode" : "xlate-pu-bdb-uni"
                    },
                    "ms": "xlate-pu-ms",
                    "ssk": "xlate-pu-ssk"
                }
            },
            "Ang":111,
            "LineNo":1,
            "SourceID":"G",
            "Transliterations":{
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            },
            "WriterID":1,
            "WriterEnglish":"writer-eng",
            "WriterGurmukhi":"writer-gurmukhi",
            "WriterUnicode":"writer-uni",
            "RaagID":1,
            "RaagGurmukhi":"raag-gurmukhi",
            "RaagUnicode":"raag-uni",
            "RaagEnglish":"raag-eng",
            "RaagWithPage":"raag(pages)",
            "SourceGurmukhi":"source-gurmukhi",
            "SourceUnicode":"source-uni",
            "SourceEnglish":"source-eng",
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, aksearch_url


def test_aksearch_ok(clear_cache, requests_mock: Mocker):
    json_blob, aksearch_url = get_aksearch_json_blob()
    requests_mock.get(f"{aksearch_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan_search(1)
    print(result)

    assert result['header_id'] == 1
    assert result['gurmukhi'] == 'head-uni'
    assert result['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }
    assert result['banis'][0]['gurmukhi_uni'] == 'index-uni'
    assert result['banis'][0]['steek'] == {
                "en": {
                    "bdb": "xlate-en-bdb",
                    "ms": "xlate-en-ms",
                    "ssk": "xlate-en-ssk"
                },
                "pu": {
                    "bdb": {
                        "gurmukhi" :"xlate-pu-bdb-gur",
                        "unicode" : "xlate-pu-bdb-uni"
                    },
                    "ms": "xlate-pu-ms",
                    "ssk": "xlate-pu-ssk"
                }
            }
    assert result['banis'][0]['writer'] == 'writer-eng'


def test_aksearch_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, aksearch_url = get_aksearch_json_blob()
    requests_mock.get(f"{aksearch_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.amritkeertan_search(1)
    print(result)

    assert result['header_id'] == 1
    assert result['gurmukhi'] != 'head'
    assert result['translit'] == {
                "en": "transliteration-en",
                "hi": "transliteration-हिं",
                "ipa": "transliteration-ɐ ɑ ɒ ɓ ɔ ɕ ɖ",
                "ur": "دھن-transliteration"
            }
    assert result['banis'][0]['gurmukhi_uni'] != 'index'
    assert result['banis'][0]['writer'] == 'writer-eng'



def test_akshabad_ok(clear_cache, requests_mock: Mocker):
    json_blob, akshabad_url = get_shabad_json_blob()
    requests_mock.get(f"{akshabad_url}", json=json_blob)

    result = amritkeertan_shabad(1111)
    print(result)

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


def test_akshabad_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, akshabad_url = get_shabad_json_blob()
    requests_mock.get(f"{akshabad_url}", json=json_blob)

    result = amritkeertan_shabad(1111)
    print(result)

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



def get_kosh_json_blob():
    kosh_url = f"{url}/kosh/n"
    result = [{"id":1,"word":"nwm","wordUni":"ਨਾਮ"}]
    json_blob = json.loads(json.dumps(result))
    return json_blob, kosh_url


def test_kosh_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_url = get_kosh_json_blob()
    requests_mock.get(f"{kosh_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh('n')
    print(result)

    assert result[0]['word'] == 'nwm'
    assert result[0]['word_uni'] == 'ਨਾਮ'

def test_kosh_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_url = get_kosh_json_blob()
    requests_mock.get(f"{kosh_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh('n')
    print(result)

    assert result[0]['word'] != 'naam'
    assert result[0]['word_uni'] == 'ਨਾਮ'


def get_kosh_word_json_blob():
    kosh_word_url = f"{url}/kosh/word/nwm"
    result = [{
        "id":1,
        "word":"nwm",
        "wordUni":"ਨਾਮ",
        "definition":"define-eng",
        "definitionUni":"define-uni"
    }]
    json_blob = json.loads(json.dumps(result))
    return json_blob, kosh_word_url


def test_kosh_word_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_word_url = get_kosh_word_json_blob()
    requests_mock.get(f"{kosh_word_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh_word('nwm')
    print(result)

    assert result[0]['word_uni'] == "ਨਾਮ"
    assert result[0]['word'] == 'nwm'
    assert result[0]['def_uni'] == 'define-uni'
    assert result[0]['def'] == 'define-eng'

def test_kosh_word_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_word_url = get_kosh_word_json_blob()
    requests_mock.get(f"{kosh_word_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh_word('nwm')
    print(result)

    assert result[0]['word_uni'] != "word-uni"
    assert result[0]['word'] != 'naam'
    assert result[0]['def_uni'] != 'uni'
    assert result[0]['def'] != 'eng'


def get_kosh_search_json_blob():
    kosh_search_url = f"{url}/kosh/search/nwm"
    result = [{
        "id":1,
        "word":"nwm",
        "wordUni":"ਨਾਮ",
        "definition":"define-eng",
        "definitionUni":"define-uni"
    }]
    json_blob = json.loads(json.dumps(result))
    return json_blob, kosh_search_url


def test_kosh_search_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_search_url = get_kosh_search_json_blob()
    requests_mock.get(f"{kosh_search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh_search('nwm')
    print(result)

    assert result[0]['word_uni'] == "ਨਾਮ"
    assert result[0]['word'] == 'nwm'
    assert result[0]['def_uni'] == 'define-uni'
    assert result[0]['def'] == 'define-eng'


def test_kosh_search_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, kosh_search_url = get_kosh_search_json_blob()
    requests_mock.get(f"{kosh_search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.kosh_search('nwm')
    print(result)

    assert result[0]['word_uni'] != "word-uni"
    assert result[0]['word'] != 'naam'
    assert result[0]['def_uni'] != 'uni'
    assert result[0]['def'] != 'eng'


def get_rehats_json_blob():
    rehats_url = f"{url}/rehats"
    result = {
        "count":1,
        "maryadas":[{
            "rehatID":1,
            "rehatName":"rehat-name",
            "alphabet":"english"
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, rehats_url


def test_rehats_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehats_url = get_rehats_json_blob()
    requests_mock.get(f"{rehats_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehats()
    print(result)

    assert result[0]['rehat_id'] == 1
    assert result[0]['rehat_name'] == 'rehat-name'

def test_rehats_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehats_url = get_rehats_json_blob()
    requests_mock.get(f"{rehats_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehats()
    print(result)

    assert result[0]['rehat_id'] == 1
    assert result[0]['rehat_name'] != 'rehat'


def get_rehat_json_blob():
    rehat_url = f"{url}/rehats/1"
    result = {
        "count":1,
        "rehatID":1,
        "chapters":[{
            "chapterID":1,
            "chapterName":"chapter-name",
            "alphabet":"english"
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, rehat_url


def test_rehat_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_url = get_rehat_json_blob()
    requests_mock.get(f"{rehat_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat(1)
    print(result)

    assert result['rehat_id'] == 1
    assert result['chapters'][0]['chapter_name'] == 'chapter-name'
    assert result['chapters'][0]['chapter_id'] == 1


def test_rehat_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_url = get_rehat_json_blob()
    requests_mock.get(f"{rehat_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat(1)
    print(result)

    assert result['rehat_id'] == 1
    assert result['chapters'][0]['chapter_name'] != 'name'
    assert result['chapters'][0]['chapter_id'] != 0


def get_rehat_chapter_json_blob():
    rehat_chapter_url = f"{url}/rehats/1/chapters/1"
    result = {
        "count":1,
        "rehatID":1,
        "chapters":[{
            "chapterID":1,
            "chapterName":"chapter-name",
            "chapterContent":"<i><b>content</b></i><br>",
            "alphabet":"english"
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, rehat_chapter_url


def test_rehat_chapter_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_chapter_url = get_rehat_chapter_json_blob()
    requests_mock.get(f"{rehat_chapter_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat_chapter(1, 1)
    print(result)

    assert result['rehat_id'] == 1
    assert result['chapter_id'] == 1
    assert result['alphabet'] == 'english'
    assert result['content'] == 'content'


def test_rehat_chapter_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_chapter_url = get_rehat_chapter_json_blob()
    requests_mock.get(f"{rehat_chapter_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat_chapter(1, 1)
    print(result)

    assert result['rehat_id'] != 0
    assert result['chapter_id'] == 1
    assert result['alphabet'] != 'eng'
    assert result['content'] == 'content'


def get_rehat_search_json_blob():
    rehat_search_url = f"{url}/rehats/search/sikh"
    result = {
        "count":1,
        "rows":[{
            "chapterID":1,
            "chapterName":"chapter-name",
            "chapterContent":"content",
            "rehatID":1,
            "rehatName":"rehat-name"
        }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, rehat_search_url


def test_rehat_search_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_search_url = get_rehat_search_json_blob()
    requests_mock.get(f"{rehat_search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat_search('sikh')
    print(result)

    assert result[0]['rehat_id'] == 1
    assert result[0]['rehat_name'] == 'rehat-name'
    assert result[0]['chapter_id'] == 1
    assert result[0]['chapter_name'] == 'chapter-name'


def test_rehat_search_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, rehat_search_url = get_rehat_search_json_blob()
    requests_mock.get(f"{rehat_search_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.rehat_search('sikh')
    print(result)

    assert result[0]['rehat_id'] == 1
    assert result[0]['rehat_name'] != 'rehat'
    assert result[0]['chapter_id'] == 1
    assert result[0]['chapter_name'] != 'chapter'
    


def get_writers_json_blob():
    writer_url = f"{url}/writers"
    result = {"rows":[{"WriterID":0},        
        {
            "WriterID":1,
            "WriterEnglish":"writer-eng",
            "WriterGurmukhi":"writer-gurmukhi",
            "WriterUnicode":"writer-uni"
    }]}
    json_blob = json.loads(json.dumps(result))
    return json_blob, writer_url


def test_writers_ok(clear_cache, requests_mock: Mocker):
    json_blob, writer_url = get_writers_json_blob()
    requests_mock.get(f"{writer_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.writers()
    print(result)

    assert result[0]['writer_id'] == 1
    assert result[0]['writer_name'] == 'writer-eng'


def test_writers_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, writer_url = get_writers_json_blob()
    requests_mock.get(f"{writer_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.writers()
    print(result)

    assert result[0]['writer_id'] != 0
    assert result[0]['writer_name'] != 'writer'


def get_raags_json_blob():
    raags_url = f"{url}/raags"
    result = {"rows":[{},
    {
        "RaagID":1,
        "RaagGurmukhi":"raag-gurmukhi",
        "RaagUnicode":"raag-uni",
        "RaagEnglish":"raag-eng",
        "RaagWithPage":"raag(pages)",
        "Overview":'overview',
        "Advanced":'advanced',
        "MusicalComposure":'music',
        "Root":'root',
        "Placement":'place',
        "SourceInfo":[{
            "SourceID":"G",
            "Start":1,
            "End":1430
        }],
        "StartTime":'start',
        "EndTime":'end',
        "CommonThemes":'themes',
        "Feeling":'feels',
        "Sargun":{
            "Aroh":'aroh',
            "Avroh":'avroh',
            "Pakar":'pakar',
            "Savar":'savar',
            "Vadi":'vadi',
            "Samvadi":'samvadi',
            "Sur":'sur',
            "Thaat":'thaat',
            "Note":'note'
        },
        "Jaati":'jaati',
        "Season":'season',
        "WritersGuru":[],
        "WritersBhagat":[],
        "Writers":[]  # Guru Nanak Dev Ji
    }]
    }
    json_blob = json.loads(json.dumps(result))
    return json_blob, raags_url


def test_raags_ok(clear_cache, requests_mock: Mocker):
    json_blob, raags_url = get_raags_json_blob()
    requests_mock.get(f"{raags_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.raags()
    print(result)

    assert result[0]['raag_id'] == 1
    assert result[0]['raag_uni'] == 'raag-uni'
    assert result[0]['raag_eng'] == 'raag-eng'

def test_raags_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, raags_url = get_raags_json_blob()
    requests_mock.get(f"{raags_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.raags()
    print(result)

    assert result[0]['raag_id'] == 1
    assert result[0]['raag_uni'] != 'uni'
    assert result[0]['raag_eng'] != 'raag'

def test_raag_ok(clear_cache, requests_mock: Mocker):
    json_blob, raags_url = get_raags_json_blob()
    requests_mock.get(f"{raags_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.raag(1)
    print(result)

    assert result[0]['raag_id'] == 1
    assert result[0]['raag_uni'] == 'raag-uni'
    assert result[0]['raag'] == 'raag-eng'
    assert result[0]['time_of_raag'] == ('start', 'end')
    assert result[0]['writers'] == []
    assert result[0]['angs'] == {'G' : [1, 1430]}

def test_raag_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, raags_url = get_raags_json_blob()
    requests_mock.get(f"{raags_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.raag(1)
    print(result)

    assert result[0]['raag_id'] == 1
    assert result[0]['raag_uni'] != 'uni'
    assert result[0]['raag'] != 'raag'
    assert result[0]['time_of_raag'] == ('start', 'end')
    assert result[0]['writers'] != [0]
    assert result[0]['angs'] == {'G' : [1, 1430]}


def get_sources_json_blob():
    sources_url = f"{url}/sources"
    result = {"rows":[
        {
            "UniqueID":1,
            "SourceID":"G",
            "SourceGurmukhi":"source-gur",
            "SourceUnicode":"source-uni",
            "SourceEnglish":"source-eng"
        }
    ]}
    json_blob = json.loads(json.dumps(result))
    return json_blob, sources_url


def test_sources_ok(clear_cache, requests_mock: Mocker):
    json_blob, sources_url = get_sources_json_blob()
    requests_mock.get(f"{sources_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.sources()
    print(result)

    assert result[0]['source_id'] == 'G'
    assert result[0]['source_uni'] == 'source-uni'
    assert result[0]['source_eng'] == 'source-eng'

def test_sources_not_ok(clear_cache, requests_mock: Mocker):
    json_blob, sources_url = get_sources_json_blob()
    requests_mock.get(f"{sources_url}", json=json_blob)

    # now run the function we are testing
    result = banidb.sources()
    print(result)

    assert result[0]['source_id'] == 'G'
    assert result[0]['source_uni'] != 'uni'
    assert result[0]['source_eng'] != 'source'


def test_search_type_ok():
    result = banidb.search_type()

    assert result[2] == 'Full Word (Gurmukhi)'
    assert result[5] == 'Ang'
    assert result[7] == 'Romanized first letter anywhere (English)'

def test_search_type_not_ok():
    result = banidb.search_type()

    assert result[0] != 'First letter'
    assert result[5] != 'Page'
