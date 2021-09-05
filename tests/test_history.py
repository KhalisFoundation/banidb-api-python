# -*- coding: utf-8 -*-
import pytest

from banidb.history import LRUCache

url = 'https://api.banidb.com/v2'
target = 'mock.dat'
cache = LRUCache(target, 25)

@pytest.fixture
def clear_cache():
    cache.clear()


@pytest.fixture()
def intialize_cache_with_shabad():
    shabad = {
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
    cache.put(1111, shabad)
    return shabad


def test_intialize_cache_with_shabad_ok(intialize_cache_with_shabad):
    result = cache.get()[1111]
    assert result == intialize_cache_with_shabad


def test_intialize_cache_with_shabad_not_ok(intialize_cache_with_shabad):
    result = cache.get()
    assert result != intialize_cache_with_shabad


def test_check_ok():
    checker = cache.check(1111)
    assert checker[0] is True

def test_check_not_ok():
    assert cache.check(1111) is not False


def test_clear_not_ok():
    assert cache.get() != {'empty': True}


def test_clear_ok(clear_cache):
    clear_cache
    assert cache.get() == {'empty': True}
