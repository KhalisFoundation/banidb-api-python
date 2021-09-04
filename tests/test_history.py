# -*- coding: utf-8 -*-
import pytest

from banidb.history import LRUCache

url = 'https://api.banidb.com/v2'
target = 'mock.dat'
cache = LRUCache(target, 25)


@pytest.fixture()
def put():
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


def test_put(put):
    result = cache.get()[1111]
    assert result == put


def test_check():
    checker = cache.check(1111)
    assert checker[0] is True


def test_clear():
    cache.clear()
    assert cache.get() == {'empty': True}
