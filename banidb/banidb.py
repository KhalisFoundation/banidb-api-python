import time

import requests

from .history import LRUCache

cache = LRUCache('cache.dat', 25)

y = time.localtime().tm_year
m = time.localtime().tm_mon
d = time.localtime().tm_mday
url = 'https://api.banidb.com/v2'


def search_type():
    types = {
        0: 'First letter each word from start (Gurmukhi)',
        1: 'First letter each word anywhere (Gurmukhi)',
        2: 'Full Word (Gurmukhi)',
        3: 'Full Word Translation (English)',
        4: 'Romanized Gurmukhi (English)',
        5: 'Ang',
        6: 'Main Letter (Gurmukhi)',
        7: 'Romanized first letter anywhere (English)'
    }
    return types


def search(query, searchtype=1, source='all', larivaar=False,
           ang=None, raag=None, writer='all', page=1, results=None):
    if len(query) > 2:
        res = f"{url}/search/{query}?"
        url_address = {
            'searchtype': searchtype,
            'source': source,
            'ang': ang,
            'raag': raag,
            'writer': writer,
            'page': page,
            'results': results
            }
        for i in url_address.keys():
            res = f"{res}{i}={url_address[i]}&"
        response = requests.get(res)
        json_blob = response.json()
        info = json_blob['resultsInfo']
        total_res = info['totalResults']
        results = {'total_results': total_res}
        current_page = info['pages']['page']
        total_pages = info['pages']['totalPages']  # Total Pages
        results['total_pages'] = total_pages
        pages = {}
        for page in range(current_page, total_pages+1):
            response = requests.get(res)
            json_blob = response.json()
            info = json_blob['resultsInfo']
            pg = f"page_{page}"
            verses = []
            for verse in json_blob['verses']:
                verse_dict = {'shabad_id': verse['shabadId']}
                if larivaar is True:
                    verse_dict['lari'] = verse['larivaar']['unicode']
                else:
                    verse_dict['verse'] = verse['verse']['unicode']
                verse_dict['steek'] = {
                    'en': verse['translation']['en']['bdb'],
                    'pu': verse['translation']['pu']['bdb']['unicode']
                    }
                verse_dict['source'] = {
                    'pu': verse['source']['unicode'],
                    'en': verse['source']['english'],
                    'ang': verse['pageNo'],
                    'raagpu': verse['raag']['unicode'],
                    'raagen': verse['raag']['english'],
                    'writer': verse['writer']['english']
                    }
                verses.append(verse_dict)
            pages[pg] = verses
            if 'nextPage' in info['pages'].keys():
                res = info['pages']['nextPage']
        results['pages_data'] = pages
        return results

    else:
        raise Exception('Query length should be >= 3!')


def shabad(shabad_id, larivaar=False):
    if larivaar is True:
        id = f"{shabad_id}lari"
    else:
        id = shabad_id
    if cache.check(id)[0] is True:
        shabad = cache.get()[id]
    else:
        link = f"{url}/shabads/{shabad_id}"
        data = requests.get(link)
        json_blob = data.json()
        info = json_blob['shabadInfo']
        shabad = {'source_uni': info['source']['unicode']}
        shabad['source_eng'] = info['source']['english']
        shabad['writer'] = info['writer']['english']
        shabad['ang'] = info['source']['pageNo']
        lines = []
        for verse in json_blob['verses']:
            line = {'verse_id': verse['verseId']}
            if larivaar is True:
                if verse['larivaar']['unicode'] is not None:
                    if verse['larivaar']['unicode'] != '':
                        line['verse'] = verse['larivaar']['unicode']
                else:
                    line['verse'] = verse['verse']['unicode']
            else:
                line['verse'] = verse['verse']['unicode']
            line['steek'] = verse['translation']
            line['transliteration'] = verse['transliteration']
            lines.append(line)
        shabad['verses'] = lines
        cache.put(id, shabad)
    return shabad


def angs(ang_no, source_id='G', larivaar=False, steek=False, translit=False):
    if source_id == 'G':
        if 0 >= ang_no or ang_no > 1430:
            raise ValueError('Ang does not exist!')
    link = f"{url}/angs/{ang_no}/{source_id}"
    response = requests.get(link)
    json_blob = response.json()
    if 'error' in json_blob.keys():
        return json_blob['data']['error']
    else:
        gurbani = {}
        if 'pageNos' in json_blob.keys():
            pages = []
            for pgno in json_blob['pageNos']:
                x = angs(pgno, source_id, larivaar, steek, translit)
                pages.append(x)
            gurbani['pages'] = pages
            return gurbani
        else:
            gurbani['source'] = {
                'source_id': json_blob['source']['sourceId'],
                'unicode': json_blob['source']['unicode'],
                'english': json_blob['source']['english'],
                'ang_no': json_blob['source']['pageNo']
                }
            page = []
            for verse in json_blob['page']:
                ang = {}
                ang['verse_id'] = verse['verseId']
                ang['shabad_id'] = verse['shabadId']
                if larivaar is True:
                    ang['verse'] = verse['larivaar']['unicode']
                else:
                    ang['verse'] = verse['verse']['unicode']
                if steek is True:
                    ang['steek'] = verse['translation']
                if translit is True:
                    ang['translit'] = verse['transliteration']
                page.append(ang)
            gurbani['page'] = page
        return gurbani


def hukamnama(year=y, month=m, day=d):
    link = f"{url}/hukamnamas/{year}/{month}/{day}"
    response = requests.get(link)
    json_blob = response.json()
    if 'error' in json_blob.keys():
        return(json_blob['data']['error'])
    else:
        hukam = {}
        bani = []
        for i in json_blob['shabads']:
            x = shabad(i['shabadInfo']['shabadId'])
            cache.put(i['shabadInfo']['shabadId'], x)
            bani.append(x)
        hukam['hukam'] = bani
        return hukam


def random(source_id='G'):
    link = f"{url}/random/{source_id}"
    response = requests.get(link)
    json_blob = response.json()
    shabad_id = json_blob['shabadInfo']['shabadId']
    gurbani = shabad(shabad_id)
    cache.put(shabad_id, gurbani)
    return gurbani


def banis():
    if cache.check('banis')[0] is True:
        gurbani = cache.get()['banis']
    else:
        link = f"{url}/banis"
        response = requests.get(link)
        json_blob = response.json()
        gurbani = {'bani_id': ['gurmukhiUni', 'transliterations']}
        for bani in json_blob:
            gurbani[bani['ID']] = []
            data = ['gurmukhi_uni', 'transliterations']
            for k in data:
                if bani[k] is not None:
                    gurbani[bani['ID']].append(bani[k])
        cache.put('banis', gurbani)
    return gurbani


def bani(bani_id, larivaar=False):
    link = f"{url}/banis/{bani_id}"
    response = requests.get(link)
    json_blob = response.json()
    info = json_blob['baniInfo']
    gurbani = {
        "info": {
            'bani_id': info['baniID'],
            'unicode': info['unicode'],
            'english': info['english'],
            'hindi': info['hindi'],
            'ipa': info['ipa'],
            'urdu': info['ur']
        }}
    gurbani['raag'] = info['raag']
    gurbani['source'] = info['source']
    verses = []
    for i in json_blob['verses']:
        verse = i['verse']
        data = {'verse_id': verse['verseId']}
        if larivaar is True:
            data['verse'] = verse['larivaar']['unicode']
        else:
            data['verse'] = verse['verse']['unicode']
        data['steek'] = verse['translation']
        data['translit'] = verse['transliteration']
        verses.append(data)
    gurbani['verses'] = verses
    return gurbani


def amritkeertan():
    if cache.check('amritkeertan')[0] is True:
        aklist = cache.get()['amritkeertan']
    else:
        link = f"{url}/amritkeertan"
        response = requests.get(link)
        json_blob = response.json()
        aklist = []
        for header in json_blob['headers']:
            data = {
                'header_id': header['HeaderID'],
                'gurmukhi_uni': header['GurmukhiUni'],
                'gurmukhi': header['Gurmukhi'],
                'translit': header['Transliterations']
                }
            aklist.append(data)
        cache.put('amritkeertan', aklist)
    return aklist


def amritkeertan_index():
    link = f"{url}/amritkeertan/index"
    response = requests.get(link)
    json_blob = response.json()
    akindices = []
    for i in json_blob['index']:
        data = {
            'index_id': i['IndexID'],
            'header_id': i['HeaderID'],
            'shabad_id': i['ShabadID'],
            'gurmukhi_uni': i['GurmukhiUni'],
            'steek': i['Translations'],
            'translit': i['Transliterations'],
            'source_id': i['SourceID'],
            'ang': i['Ang'],
            'writer': i['WriterEnglish'],
            'raag_id': i['RaagID']
        }
        fdata = {}
        for k in data:
            if data[k] is not None and data[k] != '':
                fdata[k] = data[k]
        akindices.append(fdata)
    return akindices


def amritkeertan_search(header_id):
    link = f"{url}/amritkeertan/index/{header_id}"
    response = requests.get(link)
    json_blob = response.json()
    header = json_blob['header'][0]
    results = {
        'Header ID': header['HeaderID'],
        'Gurmukhi': header['GurmukhiUni'],
        'Translit': header['Transliterations']
    }
    banis = []
    for index in json_blob['index']:
        data = {
            'index_id': index['IndexID'],
            'header_id': index['HeaderID'],
            'shabad_id': index['ShabadID'],
            'gurmukhi_uni': index['GurmukhiUni'],
            'steek': index['Translations'],
            'translit': index['Transliterations'],
            'source_id': index['SourceID'],
            'ang': index['Ang'],
            'writer': index['WriterEnglish'],
            'raag_id': index['RaagID']
        }
        banis.append(data)
    results['banis'] = banis
    return results


def amritkeertan_shabad(shabad_id):
    gurbani = shabad(shabad_id)
    return gurbani


def kosh(letter):
    link = f"{url}/kosh/{letter}"
    response = requests.get(link)
    json_blob = response.json()
    results = [['ਸ਼ਬਦ', 'Word']]
    res_count = len(json_blob)
    for i in range(res_count):
        word = json_blob[i]
        results.append([word['word_uni'], word['word']])
    return results


def kosh_word(word):
    link = f"{url}/kosh/word/{word}"
    response = requests.get(link)
    json_blob = response.json()
    results = []
    for word in json_blob:
        data = {
            'word_uni': word['wordUni'],
            'word': word['word'],
            'def_uni': word['definitionUni'],
            'def': word['definition']
        }
        results.append(data)
    return results


def kosh_search(query):
    link = f"{url}/kosh/search/{query}"
    response = requests.get(link)
    json_blob = response.json()
    results = []
    res_count = len(json_blob)
    for i in range(res_count):
        data = json_blob[i]
        results.append([data['wordUni'], data['definitionUni']])
    return results


def rehats():
    if cache.check('rehats')[0] is True:
        rehats = cache.get()['rehats']
    else:
        link = f"{url}/rehats"
        response = requests.get(link)
        json_blob = response.json()
        rehats = []
        for i in json_blob['maryadas']:
            data = {
                'rehat_id': i['rehatID'],
                'rehat_name': i['rehatName']
            }
            rehats.append(data)
        cache.put('rehats', rehats)
    return rehats


def rehat(rehat_id):
    link = f"{url}/rehats/{rehat_id}"
    response = requests.get(link)
    json_blob = response.json()
    chapters = {
        'rehat_id': rehat_id,
        'chapters': []
        }
    for i in json_blob['chapters']:
        chapter = {
            'chapter_id': i['chapterID'],
            'chapter_name': i['chapterName']
            }
        chapters['chapters'].append(chapter)
    return chapters


def rehat_chapter(rehat_id, chapter_id):
    link = f"{url}/rehats/{rehat_id}/chapters/{chapter_id}"
    response = requests.get(link)
    json_blob = response.json()
    tags = ['&', '<']
    chapter = json_blob
    content = chapter['chapters'][0]['chapterContent']
    for i in content:
        if i in tags:
            if i == '<':
                x = content.index(i)
                y = content.index('>')
                content = content[:x]+content[y+1:]
            elif i == '&':
                tag = ['&nbsp;', '&amp;']
                for j in tag:
                    content = content.replace(j, '')
    chapter['content'] = content
    return chapter


def rehat_search(query):
    link = f"{url}/rehats/search/{query}"
    response = requests.get(link)
    json_blob = response.json()
    results = [{'rehat_id': 1}]
    for i in json_blob['rows']:
        chapter = {
            'chapter_id': i['chapterID'],
            'chapter_name': i['chapterName']
            }
        results.append(chapter)
    return results


def writers():
    if cache.check('writers')[0] is True:
        writers = cache.get()['writers']
    else:
        link = f"{url}/writers"
        response = requests.get(link)
        json_blob = response.json()
        writers = []
        for row in json_blob['rows'][1:]:
            writer = {
                'writer_id': row['WriterID'],
                'writer_name': row['WriterEnglish']
                }
            writers.append(writer)
        cache.put('writers', writers)
    return writers


def raags():
    if cache.check('raags')[0] is True:
        raags = cache.get()['raags']
    else:
        link = f"{url}/raags"
        response = requests.get(link)
        json_blob = response.json()
        cache.put('raags', json_blob)
    raags = []
    for row in json_blob['rows'][1:]:
        raag = {
            'raag_id': row['RaagID'],
            'raag_uni': row['RaagUnicode'],
            'raag_eng': row['RaagEnglish']
            }
        raags.append(raag)
    return raags


def raag(raag_id):
    if 'raags' in cache.get().keys():
        json_blob = cache.get()['raags']
    else:
        link = f"{url}/raags"
        response = requests.get(link)
        json_blob = response.json()
    result = []
    for row in json_blob['rows'][1:]:
        if row['RaagID'] == raag_id:
            writer_url = f"{url}/writers"
            wres = requests.get(writer_url)
            wjs = wres.json()
            info = row['SourceInfo'][0]
            raag_data = {}
            data = {
                'raag_id': row['RaagID'],
                'raag_uni': row['RaagUnicode'],
                'raag': row['RaagEnglish']+'\n',
                'time_of_raag': (row['StartTime'], row['EndTime']),
                'common_themes': row['CommonThemes'],
                'feeling': row['Feeling'],
                'angs': {info['SourceID']: [info['Start'], info['End']]},
                'overview': row['Overview'],
                'advanced': row['Advanced'],
                'musical_composure': row['MusicalComposure'],
                'placement': row['Placement'],
                'season': row['Season'],
                'sargun': '',
                'aroh': row['Sargun']['Aroh'],
                'avroh': row['Sargun']['Avroh'],
                'vadi': row['Sargun']['Vadi'],
                'samvadi': row['Sargun']['Samvadi'],
                'sur': row['Sargun']['Sur'],
                'thaat': row['Sargun']['Thaat'],
                'jaati': row['Jaati']
                }
            data['writers'] = []
            for writer in row['Writers']:  # provides list of writer names
                for writer_row in wjs['rows']:
                    if writer_row['WriterID'] == writer:
                        data['writers'].append(writer_row['WriterEnglish'])
            for k in data.keys():  # removes empty or null data values
                if data[k] is not None and data[k] != '':
                    raag_data[k] = data[k]
            result.append(raag_data)
    return result


def sources():
    if 'sources' in cache.get().keys():
        result = cache.get()['sources']
    else:
        link = f"{url}/sources"
        response = requests.get(link)
        json_blob = response.json()
        result = []
        for row in json_blob['rows']:
            source = {
                'source_id': row['SourceID'],
                'source_uni': row['SourceUnicode'],
                'source_eng': row['SourceEnglish']
                }
            result.append(source)
        cache.put('sources', result)
    return result


def history():
    hist = cache.get()
    result = hist
    if 'empty' not in hist.keys():
        data = list(hist.keys())  # lru as a stack
        if data != []:
            data = data[len(data)::-1]
            result = f"Frequently used data: {data}"
    return result


def clear():
    hist = cache.get()
    if 'empty' not in hist:
        cache.clear()
