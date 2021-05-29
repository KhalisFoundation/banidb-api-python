import requests
import time
from functools import lru_cache
y = time.localtime().tm_year
m = time.localtime().tm_mon
d = time.localtime().tm_mday
url = 'https://api.banidb.com/v2'


def searchtype():
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


@lru_cache(maxsize=5)
def search(query, searchtype=1, source='all', larivaar=False,
           ang=None, raag=None, writer='all', page=1, results=None):
    res = url+'/search/'+str(query)+'?'
    urladd = {
        'searchtype': searchtype,
        'source': source,
        'ang': ang,
        'raag': raag,
        'writer': writer,
        'page': page,
        'results': results
        }
    for i in urladd.keys():
        res += i+'='+str(urladd[i])+'&'
    results = {}
    response = requests.get(res)
    js = response.json()
    info = js['resultsInfo']
    total_res = info['totalResults']
    results['totalResults'] = total_res
    current_page = info['pages']['page']
    total_pages = info['pages']['totalPages']  # Total Pages
    results['totalPages'] = total_pages
    pages = {}
    for page in range(current_page, total_pages+1):
        response = requests.get(res)
        js = response.json()
        info = js['resultsInfo']
        pg = 'Page'+str(page)
        verses = []
        for verse in js['verses']:
            verse_dict = {}
            verse_dict['shabadId'] = verse['shabadId']
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
    results['pagesData'] = pages
    return results


@lru_cache(maxsize=5)  # understand and use everywhere
def shabad(shabad_id, larivaar=False):
    link = url+'/shabads/'+str(shabad_id)
    data = requests.get(link)
    js = data.json()
    info = js['shabadInfo']
    shabad = {}
    shabad['sourceUni'] = info['source']['unicode']
    shabad['sourceEng'] = info['source']['english']
    shabad['writer'] = info['writer']['english']
    shabad['ang'] = info['source']['pageNo']
    lines = []
    for verse in js['verses']:
        line = {}
        line['verseID'] = verse['verseId']
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
    return shabad


def angs(ang_no, source_id='G', larivaar=False, steek=False, translit=False):
    if source_id == 'G':
        if 0 >= ang_no or ang_no > 1430:
            raise ValueError('Ang does not exist!')
    link = url+'/angs/'+str(ang_no)+'/'+str(source_id)
    response = requests.get(link)
    js = response.json()
    if 'error' in js.keys():
        return js['data']['error']
    else:
        gurbani = {}
        if 'pageNos' in js.keys():
            pages = []
            for pgno in js['pageNos']:
                x = angs(pgno, source_id, larivaar, steek, translit)
                pages.append(x)
            gurbani['pages'] = pages
            return gurbani
        else:
            gurbani['source'] = {
                'sourceId': js['source']['sourceId'],
                'unicode': js['source']['unicode'],
                'english': js['source']['english'],
                'angNo': js['source']['pageNo']
                }
            page = []
            for verse in js['page']:
                ang = {}
                ang['verseId'] = verse['verseId']
                ang['shabadId'] = verse['shabadId']
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


@lru_cache(maxsize=1)
def hukamnama(year=y, month=m, day=d):
    link = url+'/hukamnamas/'+str(year)+'/'+str(month)+'/'+str(day)
    response = requests.get(link)
    js = response.json()
    if 'error' in js.keys():
        return(js['data']['error'])
    else:
        hukam = {}
        bani = []
        for i in js['shabads']:
            x = shabad(i['shabadInfo']['shabadId'])
            bani.append(x)
        hukam['hukam'] = bani
        return hukam


def random(source_id='G'):
    link = url+'/random/'+source_id
    response = requests.get(link)
    js = response.json()
    gurbani = shabad(js['shabadInfo']['shabadId'])
    return gurbani


@lru_cache(maxsize=1)
def banis():
    link = url+"/banis"
    response = requests.get(link)
    js = response.json()
    gurbani = {'Bani ID': ['gurmukhiUni', 'transliterations']}
    for bani in js:
        gurbani[bani['ID']] = []
        data = ['gurmukhiUni', 'transliterations']
        for k in data:
            if bani[k] is not None:
                gurbani[bani['ID']].append(bani[k])
    return gurbani


def bani(bani_id, larivaar=False):
    link = url+"/banis/"+str(bani_id)
    response = requests.get(link)
    js = response.json()
    gurbani = {}
    info = js['baniInfo']
    gurbani["Info"] = {
        'baniID': info['baniID'],
        'unicode': info['unicode'],
        'english': info['english'],
        'hindi': info['hindi'],
        'ipa': info['ipa'],
        'urdu': info['ur']
        }
    gurbani['raag'] = info['raag']
    gurbani['source'] = info['source']
    verses = []
    for i in js['verses']:
        verse = i['verse']
        data = {}  # shall be converted to easily accessible dictionary
        data['verseId'] = verse['verseId']
        if larivaar is True:
            data['verse'] = verse['larivaar']['unicode']
        else:
            data['verse'] = verse['verse']['unicode']
        data['steek'] = verse['translation']
        data['translit'] = verse['transliteration']
        verses.append(data)
    gurbani['Verse'] = verses
    return gurbani


@lru_cache(maxsize=1)
def amritkeertan():
    link = url+'/amritkeertan'
    response = requests.get(link)
    js = response.json()
    aklist = []
    for header in js['headers']:
        data = {
            'Header ID': header['HeaderID'],
            'GurmukhiUni': header['GurmukhiUni'],
            'Gurmukhi': header['Gurmukhi'],
            'Translit': header['Transliterations']
            }
        aklist.append(data)
    return aklist


@lru_cache(maxsize=1)
def amritkeertanindex():
    link = url+'/amritkeertan/index'
    response = requests.get(link)
    js = response.json()
    akindices = {}
    for i in js['index']:
        data = {
            'IndexID': i['IndexID'],
            'HeaderID': i['HeaderID'],
            'ShabadID': i['ShabadID'],
            'Gurmukhi': i['GurmukhiUni'],
            'Steek': i['Translations'],
            'Translit': i['Transliterations'],
            'SourceID': i['SourceID'],
            'Ang': i['Ang'],
            'Writer': i['WriterEnglish'],
            'RaagID': i['RaagID']
        }
        fdata = {}
        for k in data:
            if data[k] is not None and data[k] != '':
                fdata[k] = data[k]
        akindices[i['IndexID']] = fdata
    return akindices


def amritkeertansearch(header_id):
    link = url+'/amritkeertan/index/'+str(header_id)
    response = requests.get(link)
    js = response.json()
    results = {}
    header = js['header'][0]
    results['Header ID'] = header['HeaderID']
    results['Gurmukhi'] = header['GurmukhiUni']
    results['Translit'] = header['Transliterations']
    banis = []
    for index in js['index']:
        data = {
            'IndexID': index['IndexID'],
            'HeaderID': index['HeaderID'],
            'ShabadID': index['ShabadID'],
            'Gurmukhi': index['GurmukhiUni'],
            'Steek': index['Translations'],
            'Translit': index['Transliterations'],
            'SourceID': index['SourceID'],
            'Ang': index['Ang'],
            'Writer': index['WriterEnglish'],
            'RaagID': index['RaagID']
        }
        banis.append(data)
    results['Banis'] = banis
    return results


def amritkeertanshabad(shabad_id):
    gurbani = shabad(shabad_id)
    return gurbani


def kosh(letter):
    link = url+'/kosh/'+str(letter)
    response = requests.get(link)
    js = response.json()
    results = [['ਸ਼ਬਦ', 'Word']]
    res_count = len(js)
    for i in range(res_count):
        word = js[i]
        results.append([word['wordUni'], word['word']])
    return results


def koshword(word):
    link = url+'/kosh/word/'+str(word)
    response = requests.get(link)
    js = response.json()
    results = []
    for word in js:
        data = {
            'wordUni': word['wordUni'],
            'word': word['word'],
            'defUni': word['definitionUni'],
            'def': word['definition']
        }
        results.append(data)
    return results


def koshsearch(query):
    link = url+'/kosh/search/'+str(query)
    response = requests.get(link)
    js = response.json()
    results = []
    res_count = len(js)
    for i in range(res_count):
        data = js[i]
        results.append([data['wordUni'], data['definitionUni']])
    return results


@lru_cache(maxsize=1)
def rehats():
    link = url+'/rehats'
    response = requests.get(link)
    js = response.json()
    rehats = []
    for i in js['maryadas']:
        data = {
            'rehatID': i['rehatID'],
            'rehatName': i['rehatName']
        }
        rehats.append(data)
    return rehats


def rehat(rehat_id):
    link = url+'/rehats/'+str(rehat_id)
    response = requests.get(link)
    js = response.json()
    chapters = {
        'Rehat ID': rehat_id,
        'chapters': []
        }
    for i in js['chapters']:
        chapter = {
            'Chapter ID': i['chapterID'],
            'Chapter Name': i['chapterName']
            }
        chapters['chapters'].append(chapter)
    return chapters


def rehatchapter(rehat_id, chapter_id):
    link = url+'/rehats/'+str(rehat_id)+'/chapters/'+str(chapter_id)
    response = requests.get(link)
    js = response.json()
    tags = ['&', '<']
    chapter = js
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


def rehatsearch(query):  # remove extra html tags from API
    link = url+'/rehats/search/'+str(query)
    response = requests.get(link)
    js = response.json()
    results = []
    for i in js['rows']:
        chapter = {
            'chapterID': i['chapterID'],
            'chapterName': i['chapterName']
            }
        results.append(chapter)
    return results


@lru_cache(maxsize=1)
def writers():
    link = url+'/writers'
    response = requests.get(link)
    js = response.json()
    writers = []
    for row in js['rows'][1:]:
        writer = {
            'WriterID': row['WriterID'],
            'WriterName': row['WriterEnglish']
            }
        writers.append(writer)
    return writers


@lru_cache(maxsize=1)
def raags():
    link = url+'/raags'
    response = requests.get(link)
    js = response.json()
    raags = []
    for row in js['rows'][1:]:
        raag = {
            'RaagID': row['RaagID'],
            'RaagUni': row['RaagUnicode'],
            'RaagEng': row['RaagEnglish']
            }
        raags.append(raag)
    return raags


@lru_cache(maxsize=50)
def raag(raag_id):
    link = url+'/raags'
    response = requests.get(link)
    js = response.json()
    result = []
    for row in js['rows'][1:]:
        if row['RaagID'] == raag_id:
            writer_url = url+'/writers'
            wres = requests.get(writer_url)
            wjs = wres.json()
            info = row['SourceInfo'][0]
            raag_data = {}
            data = {
                'Raag ID': row['RaagID'],
                'ਰਾਗੁ': row['RaagUnicode'],
                'Raag': row['RaagEnglish']+'\n',
                'TimeOfRaag': (row['StartTime'], row['EndTime']),
                'CommonThemes': row['CommonThemes'],
                'Feeling': row['Feeling'],
                'Angs': {info['SourceID']: [info['Start'], info['End']]},
                'Overview': row['Overview'],
                'Advanced': row['Advanced'],
                'MusicalComposure': row['MusicalComposure'],
                'Placement': row['Placement'],
                'Season': row['Season'],
                'Sargun': '',
                'Aroh': row['Sargun']['Aroh'],
                'Avroh': row['Sargun']['Avroh'],
                'Vadi': row['Sargun']['Vadi'],
                'Samvadi': row['Sargun']['Samvadi'],
                'Sur': row['Sargun']['Sur'],
                'Thaat': row['Sargun']['Thaat'],
                'Jaati': row['Jaati']
                }
            data['Writers'] = []
            for writer in row['Writers']:  # provides list of writer names
                for writer_row in wjs['rows']:
                    if writer_row['WriterID'] == writer:
                        data['Writers'].append(writer_row['WriterEnglish'])
            for k in data.keys():  # removes empty or null data values
                if data[k] is not None and data[k] != '':
                    raag_data[k] = data[k]
            result.append(raag_data)
    return result


@lru_cache(maxsize=1)
def sources():
    link = url+'/sources'
    response = requests.get(link)
    js = response.json()
    result = []
    for row in js['rows']:
        source = {
            'SourceID': row['SourceID'],
            'SourceUni': row['SourceUnicode'],
            'SourceEng': row['SourceEnglish']
            }
        result.append(source)
    return result
