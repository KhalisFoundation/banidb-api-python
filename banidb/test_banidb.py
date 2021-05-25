# -*- coding: utf-8 -*-
import requests
import pytest
import banidb.banidb


def test_backend_up():
    js = requests.get('https://api.banidb.com/v2/health').json()
    assert js['ok'] is True


def test_searchtype():
    res = banidb.searchtype()
    assert res == {
        0: 'First letter each word from start (Gurmukhi)',
        1: 'First letter each word anywhere (Gurmukhi)',
        2: 'Full Word (Gurmukhi)',
        3: 'Full Word Translation (English)',
        4: 'Romanized Gurmukhi (English)',
        5: 'Ang',
        6: 'Main Letter (Gurmukhi)',
        7: 'Romanized first letter anywhere (English)'
    }


def test_random():
    x = banidb.random()
    assert type(x) == dict


def test_search():
    x = banidb.search('jjrlAkD')
    assert x == {'totalResults': 1, 'totalPages': 1, 'pagesData': {'Page1': [{'shabadId': 3192, 'verse': 'ਜਗਤੁ ਜਲੰਦਾ ਰਖਿ ਲੈ ਆਪਣੀ ਕਿਰਪਾ ਧਾਰਿ ॥', 'steek': {'en': {'bdb': 'The world is going up in flames - shower it with Your Mercy, and save it!', 'ms': 'O Lord, the world is on fire. Showering thy benediction save it Thou.', 'ssk': 'The world is going up in flames - shower it with Your Mercy, and save it!'}, 'pu': {'ss': {'gurmukhi': 'hy pRBU! (ivkwrW ivc) sV rhy sMswr ƒ AwpxI imhr kr ky bcw lY, ', 'unicode': 'ਹੇ ਪ੍ਰਭੂ! (ਵਿਕਾਰਾਂ ਵਿਚ) ਸੜ ਰਹੇ ਸੰਸਾਰ ਨੂੰ ਆਪਣੀ ਮਿਹਰ ਕਰ ਕੇ ਬਚਾ ਲੈ, '}, 'ft': {'gurmukhi': 'ieh jgq kwm, kRoD, iqRSnw kI AgnI myN jo jl irhw hY, hy vwihgurU! iqs ko vw iqs jgq sy myry ko qum ApxI ikrpw Dwr ky rKÎw kr lyvo]', 'unicode': 'ਇਹ ਜਗਤ ਕਾਮ, ਕ੍ਰੋਧ, ਤ੍ਰਿਸ਼ਨਾ ਕੀ ਅਗਨੀ ਮੇਂ ਜੋ ਜਲ ਰਿਹਾ ਹੈ, ਹੇ ਵਾਹਿਗੁਰੂ! ਤਿਸ ਕੋ ਵਾ ਤਿਸ ਜਗਤ ਸੇ ਮੇਰੇ ਕੋ ਤੁਮ ਅਪਣੀ ਕਿਰਪਾ ਧਾਰ ਕੇ ਰਖ੍ਯਾ ਕਰ ਲੇਵੋ॥'}, 'bdb': {'gurmukhi': 'hy pRBU! (ivkwrW ivc) sV rhy sMswr ƒ AwpxI imhr kr ky bcw lY, ', 'unicode': 'ਹੇ ਪ੍ਰਭੂ! (ਵਿਕਾਰਾਂ ਵਿਚ) ਸੜ ਰਹੇ ਸੰਸਾਰ ਨੂੰ ਆਪਣੀ ਮਿਹਰ ਕਰ ਕੇ ਬਚਾ ਲੈ, '}, 'ms': {'gurmukhi': 'hy suAwmI! sMswr sV bl irhw hY[ AwpxI rihmq kr ky qUM ies dI r`iKAw kr[', 'unicode': 'ਹੇ ਸੁਆਮੀ! ਸੰਸਾਰ ਸੜ ਬਲ ਰਿਹਾ ਹੈ। ਆਪਣੀ ਰਹਿਮਤ ਕਰ ਕੇ ਤੂੰ ਇਸ ਦੀ ਰੱਖਿਆ ਕਰ।'}}, 'es': {'sn': 'El mundo está en llamas; oh Dios, sálvalo por Misericordia. '}, 'hi': {'ss': 'हे प्रभू ! (विकारों में) जल रहे संसार को अपनी मेहर से बचा लें।', 'sts': 'हे परमात्मा ! यह जगत् तृष्णाग्नि में जल रहा है, अपनी कृपा करके इसकी रक्षा करो।'}}, 'source': {'pu': 'ਸ੍ਰੀ ਗੁਰੂ ਗ੍ਰੰਥ ਸਾਹਿਬ ਜੀ', 'en': 'Sri Guru Granth Sahib Ji', 'ang': 853, 'raagpu': 'ਰਾਗੁ ਬਿਲਾਵਲ', 'raagen': 'Raag Bilaaval', 'writer': 'Guru Amar Daas Ji'}}]}}
