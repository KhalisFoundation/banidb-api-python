import requests
import time
y,m,d=time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday
source={
        'G': 'Guru Granth Sahib Ji',
        'D': 'Dasam Granth Sahib',
        'B': 'Bhai Gurdas Ji Vaaran',
        'A':'Amrit Keertan',
        'S': 'Bhai Gurdas Singh Ji Vaaran',
        'N': 'Bhai Nand Lal Ji Vaaran',
        'R': 'Rehatnamas & Panthic Sources'
        }

def run(link):
    q=requests.get(link)
    r=q.json()
    for j in r['verses']:
        print('Shabad Id: ',j['shabadId'])
        l=[j['verse']['unicode'],j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode'],[j['source']['english'],'-',j['source']['pageNo'],', ',j['writer']['english'],' ',j['raag']['english']]]
        for k in l:
            if k!=None:
                if type(k)==list:
                    for m in k:
                        print(m,end='')
                    continue
                print(k)
        print('\n')
    return r

def search(query,searchtype=1,source='all',ang=None,raag=None,writer='all',page=1,results=None):
    res='https://api.banidb.com/v2/search/'+str(query)+'?'
    s={
        'searchtype':searchtype,
        'source':source,
        'ang':ang,
        'raag':raag,
        'writer':writer,
        'page':page,
        'results':results
        }
    for i in s.keys():
        res+=i+'='+str(s[i])+'&'
    response=requests.get(res)
    result=response.json()
    info=result['resultsInfo']
    totalRes=info['totalResults'] #Total Shabads found!
    totalPages=info['pages']['totalPages'] #Total Pages
    for k in range(1,totalPages+1):
        info=result['resultsInfo']
        print('Search results for Page ',k,'\n')
        result=run(res)
        if 'nextPage' in info['pages'].keys():
            res=info['pages']['nextPage']
            
#Updated on 19/04/2021 - 20:26 IST

def shabad(shabadID):                     #used for getting specific shabad using Shabad ID which we get from search()
    link='https://api.banidb.com/v2/shabads/'+str(shabadID)
    q=requests.get(link)
    r=q.json()
    s=r['shabadInfo']
    print('\n')
    print(s['source']['unicode'],'-','ਅੰਗ',s['source']['pageNo'])
    print(s['writer']['english'],'-',s['source']['english'],'-','Ang',s['source']['pageNo'])
    print('\n')
    for j in r['verses']:
        l=[j['verse']['unicode'],j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode']]
        for k in l:
            if k!=None:
                print(k)
        print('\n')

#Updated on 19/04/2021 - 00:26 IST
def angs(angNo,sourceID='G'):
    link='https://api.banidb.com/v2/angs/'+str(angNo)+'/'+str(sourceID)
    q=requests.get(link)
    r=q.json()
    if 'pageNos' in r.keys():
        for i in r['pages']:
            print('\n')
            print(i['source']['unicode'],'-','ਅੰਗ',i['source']['pageNo'])
            print(i['source']['english'],'-','Ang',i['source']['pageNo'])
            print('\n')
            for j in i['page']:
                l=[j['verse']['unicode'],j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode']]
                for k in l:
                    if k!=None:
                        print(k)
                print('\n')
    else:
        print('\n')
        print(r['source']['unicode'],'-','ਅੰਗ',r['source']['pageNo'])
        print(r['source']['english'],'-','Ang',r['source']['pageNo'])
        print('\n')
        for j in r['page']:
            l=[j['verse']['unicode'],j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode']]
            for k in l:
                if k!=None:
                    print(k)
            print('\n')

#Updated on 21/04/2021 - 13:01 IST
def hukamnama(year=y,month=m,day=d):
    link='https://api.banidb.com/v2/hukamnamas/'+str(year)+'/'+str(month)+'/'+str(day)
    q=requests.get(link)
    r=q.json()
    if 'error' in r.keys():
        print(r['data']['error'])
    else:
        for i in r['shabadIds']:
            shabad(i)

#Updated on 20/04/2021 - 01:21 IST
def random(sourceID='G'):
    print('Source -',source[sourceID])
    link='https://api.banidb.com/v2/random/'+sourceID
    q=requests.get(link)
    r=q.json()
    print('\n')
    print(r['shabadInfo']['raag']['unicode'],'-',r['shabadInfo']['source']['unicode'],'-','ਅੰਗ',r['shabadInfo']['source']['pageNo'])
    print(r['shabadInfo']['raag']['english'],'-',r['shabadInfo']['writer']['english'],'-',r['shabadInfo']['source']['english'],'-','Ang',r['shabadInfo']['source']['pageNo'])
    print('\n')
    for j in r['verses']:
        l=[j['verse']['unicode'],j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode']]
        for k in l:
            if k!=None:
                print(k)
        print('\n')

#Updated on 20/04/2021 - 22:51 IST
def banis():
    link="http://api.banidb.com/v2/banis"
    q=requests.get(link)
    r=q.json()
    print('List of Banis found in Sundar Gutka\n')
    for i in r:
        print('Bani ID:',i['ID'])
        l=[i['gurmukhiUni'],i['transliteration']]
        for k in l:
            if k!=None:
                print(k)
        print('\n')

#Updated on 21/04/2021 - 00:46 IST
def bani(baniID):
    link="http://api.banidb.com/v2/banis/"+str(baniID)
    q=requests.get(link)
    r=q.json()
    info=r['baniInfo']
    print(info['unicode'],info['english'],sep='\n')
    if info['source']['unicode'] != None:
        print(info['source']['unicode'],info['source']['english'],sep='\n')
    print('\n\n')
    for i in r['verses']:
        b=i['verse']
        l=[b['verse']['unicode'],b['translation']['en']['bdb']]
        if 'bdb' in b['translation']['pu'].keys():
            l.append(b['translation']['pu']['bdb']['unicode'])
        for k in l:
            if k!=None:
                print(k)
        print('\n')

def amritkeertan():
    link='http://api.banidb.com/v2/amritkeertan'
    q=requests.get(link)
    r=q.json()
    for i in r['headers']:
        l={'Header ID':i['HeaderID'],'Gurmukhi':i['GurmukhiUni'],'English':i['Transliterations']['en']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def amritkeertanindex():
    link='http://api.banidb.com/v2/amritkeertan/index'
    q=requests.get(link)
    r=q.json()
    for i in r['index']:
        print('Header ID','-',i['HeaderID'])
        print('Shabad ID','-',i['ShabadID'])
        l=[i['GurmukhiUni'],i['Translations']['en']['bdb'],i['Translations']['puu']['bdb']]
        for k in l:
            if k!=None:
                print(k)
        print('\n')

def amritkeertansearch(headerID):
    link='http://api.banidb.com/v2/amritkeertan/index/'+str(headerID)
    q=requests.get(link)
    r=q.json()
    h=r['header'][0]
    print('Header ID','-',h['HeaderID'],'\n')
    print(h['GurmukhiUni'])
    print(h['Transliterations']['en'])
    print('\n')
    for i in r['index']:
        print('Shabad ID','-',i['ShabadID'])
        l=[i['GurmukhiUni'],i['Translations']['en']['bdb'],i['Transliterations']['en'],i['WriterUnicode'],i['WriterEnglish'],i['SourceUnicode']+' ('+i['SourceEnglish']+')']
        for k in l:
            if k!=None:
                print(k)
        print('\n')

def amritkeertanshabad(shabadID):
    shabad(shabadID)

def kosh(letter):
    link='http://api.banidb.com/v2/kosh/'+str(letter)
    q=requests.get(link)
    r=q.json()
    print('\n')
    for i in range(len(r)):
        f=r[i]
        print('ਸ਼ਬਦ:',f['wordUni'])
        print('Word:',f['word'])
        print('\n')
        if (i+1)%10==0:
            x=input('Next Page (n):')
            if x.lower()=='n':
                continue
            else:
                break

def koshword(word):
    link='http://api.banidb.com/v2/kosh/word/'+str(word)
    q=requests.get(link)
    r=q.json()
    print('\n')
    for i in r:
        print('ਸ਼ਬਦ (Word):',i['wordUni'])
        print('ਵਿਆਖਿਆ (Definition):',i['definitionUni'])
        print('\n')

def koshsearch(query):
    link='http://api.banidb.com/v2/kosh/search/'+str(query)
    q=requests.get(link)
    r=q.json()
    print('\n')
    for i in range(len(r)):
        f=r[i]
        print('ਸ਼ਬਦ (Word):',f['wordUni'])
        print('ਵਿਆਖਿਆ (Definition):',f['definitionUni'])
        print('\n')
        if (i+1)%10==0:
            x=input('Next Page (n):')
            if x.lower()=='n':
                continue
            else:
                break

def rehats():
    link='http://api.banidb.com/v2/rehats'
    q=requests.get(link)
    r=q.json()
    for i in r['maryadas']:
        l={'Rehat ID':i['rehatID'],'Rehat Name':i['rehatName']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def rehat(rehatID):
    link='http://api.banidb.com/v2/rehats/'+str(rehatID)
    q=requests.get(link)
    r=q.json()
    print('Rehat ID:',rehatID)
    for i in r['chapters']:
        l={'Chapter ID':i['chapterID'],'Chapter Name':i['chapterName']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def rehatChapter(rehatID,chapterID):
    link='http://api.banidb.com/v2/rehats/'+str(rehatID)+'/chapters/'+str(chapterID)
    q=requests.get(link)
    r=q.json()
    print('Rehat ID:',rehatID)
    for i in r['chapters']:
        l={'Chapter ID':i['chapterID'],'Chapter Name':i['chapterName'],'Chapter Content':i['chapterContent']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def rehatSearch(query):
    link='http://api.banidb.com/v2/rehats/search/'+str(query)
    q=requests.get(link)
    r=q.json()
    for i in r['rows']:
        l={'Rehat ID':i['rehatID'],'Chapter ID':i['chapterID'],'Chapter Name':i['chapterName']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def writers():
    link='http://api.banidb.com/v2/writers'
    q=requests.get(link)
    r=q.json()
    for i in r['rows'][1:]:
        l={'Writer ID':i['WriterID'],'Writer Name':i['WriterEnglish']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

#Updated on 21/04/2021 - 16:16 IST
def raags():
    link='http://api.banidb.com/v2/raags'
    q=requests.get(link)
    r=q.json()
    for i in r['rows'][1:]:
        l={
            'Raag ID':i['RaagID'],
            'ਰਾਗ':i['RaagUnicode'],
            'Raag':i['RaagEnglish']
            }
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')

def raag(RaagID):
    link='http://api.banidb.com/v2/raags'
    q=requests.get(link)
    r=q.json()
    for i in r['rows'][1:]:
        if i['RaagID']==RaagID:
            linkw='http://api.banidb.com/v2/writers'
            qw=requests.get(linkw)
            w=q.json()
            l={
                'Raag ID':i['RaagID'],
                'ਰਾਗੁ':i['RaagUnicode'],
                'Raag':i['RaagEnglish']+'\n',
                'Time of Raag':(i['StartTime'],i['EndTime']),
                'Common Themes':i['CommonThemes'],
                'Feeling':i['Feeling'],
                'Angs':source[i['SourceInfo']['SourceID']]+' - ('+str(i['SourceInfo']['Start'])+'-'+str(i['SourceInfo']['End'])+')',
                'Overview':i['Overview'],
                'Advanced':i['Advanced'],
                'Musical Composure':i['MusicalComposure'],
                'Placement':i['Placement'],
                'Season':i['Season'],
                'Writers':i['Writers'],
                'Sargun':'',
                'Aroh':i['Sargun']['Aroh'],
                'Avroh':i['Sargun']['Avroh'],
                'Vadi':i['Sargun']['Vadi'],
                'Samvadi':i['Sargun']['Samvadi'],
                'Sur':i['Sargun']['Sur'],
                'Thaat':i['Sargun']['Thaat'],
                'Jaati':i['Sargun']['Jaati']
                }
            for k in l.keys():
                if l[k]!=None:
                    print(k,'-',l[k])
            print('\n')


def sources():
    link='http://api.banidb.com/v2/sources'
    q=requests.get(link)
    r=q.json()
    for i in r['rows']:
        l={'Source ID':i['SourceID'],'Source':'',i['SourceUnicode']+'\n':i['SourceEnglish']}
        for k in l.keys():
            if l[k]!=None:
                print(k,'-',l[k])
        print('\n')