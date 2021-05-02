import requests
import time
import pickle
y,m,d=time.localtime().tm_year,time.localtime().tm_mon,time.localtime().tm_mday

def searchType():
    d={
        0: 'First letter each word from start (Gurmukhi)',
        1: 'First letter each word anywhere (Gurmukhi)',
        2: 'Full Word (Gurmukhi)',
        3: 'Full Word Translation (English)',
        4: 'Romanized Gurmukhi (English)',
        5: 'Ang',
        6: 'Main Letter (Gurmukhi)',
        7: 'Romanized first letter anywhere (English)'
    }
    return d

def search(query,searchtype=1,source='all',larivaar=False,teeka=['bdb'],ang=None,raag=None,writer='all',page=1,results=None):
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
    d={}
    response=requests.get(res)
    result=response.json()
    info=result['resultsInfo']
    totalRes=info['totalResults'] #Total Shabads found!
    totalPages=info['pages']['totalPages'] #Total Pages
    for k in range(1,totalPages+1):
        response=requests.get(res)
        r=response.json()
        info=r['resultsInfo']
        s='Page'+str(k)
        ver=[]
        for j in r['verses']:
            v={}
            v['shabadId']=j['shabadId']
            if larivaar==True:
                v['lari']=j['larivaar']['unicode']
            else:
                v['verse']=j['verse']['unicode']
            t={'en':[],'pu':[],'hi':[],'es':[]}
            for h in teeka:
                trans=j['translation']
                for g in trans.keys():
                    if h in trans[g].keys():
                        t[g].append(trans[g][h])
            v['teeka']=t
            v['source']={'pu':j['source']['unicode'],'en':j['source']['english'],'ang':j['pageNo'],'raagpu':j['raag']['unicode'],'raagen':j['raag']['english'],'writer':j['writer']['english']}
            ver.append(v)
        d[s]=ver
        if 'nextPage' in info['pages'].keys():
            res=info['pages']['nextPage']
    return d

def shabad(shabadID,larivaar=False,teeka=['bdb']):                     #used for getting specific shabad using Shabad ID which we get from search()
    link='https://api.banidb.com/v2/shabads/'+str(shabadID)
    q=requests.get(link)
    save({'shabadID':shabadID})
    r=q.json()
    s=r['shabadInfo']
    d={}
    d['sourceUni']=s['source']['unicode']
    d['sourceEng']=s['source']['english']
    d['writer']=s['writer']['english'] 
    d['ang']=s['source']['pageNo']
    e=[]
    for j in r['verses']:
        v={}
        if larivaar==True:
            if j['larivaar']['unicode']!=None and j['larivaar']['unicode']!='':
                v['verse']=j['larivaar']['unicode']
            else:
                v['verse']=j['verse']['unicode']
        else:
            v['verse']=j['verse']['unicode']
        t={'en':[],'pu':[],'hi':[],'es':[]}
        for h in teeka:
            trans=j['translation']
            for g in trans.keys():
                if h in trans[g].keys():
                    t[g].append(trans[g][h])
        v['teeka']=t
        e.append(v)
    d['verses']=e
    return d

def angs(angNo,sourceID='G',larivaar=False,translation=False):
    link='https://api.banidb.com/v2/angs/'+str(angNo)+'/'+str(sourceID)
    q=requests.get(link)
    r=q.json()
    d={}
    if 'pageNos' in r.keys():
        d['source']=[r['pages'][0]['source']['unicode'],r['pages'][0]['source']['english']]
        for i in r['pageNos']:
            pg='Ang'+str(i)
            x=angs(i)
            d[pg]= x[pg]
    else:
        d['source']=[r['source']['unicode'],r['source']['english']]
        pg='Ang'+str(r['source']['pageNo'])
        ver=[]
        for j in r['page']:
            l=[]
            if larivaar==True:
                l.append(j['larivaar']['unicode'])
            else:
                l.append(j['verse']['unicode'])
            if translation==True:
                l.append(j['translation']['en']['bdb'],j['translation']['pu']['bdb']['unicode'])
            p=[]
            for k in l:
                if k!=None:
                    p.append(k)
            ver.append(p)
        d[pg]=ver
    return d

def hukamnama(year=y,month=m,day=d):
    link='https://api.banidb.com/v2/hukamnamas/'+str(year)+'/'+str(month)+'/'+str(day)
    q=requests.get(link)
    r=q.json()
    if 'error' in r.keys():
        return(r['data']['error'])
    else:
        for i in r['shabadIds']:
            save({'shabadID':i})
            x=shabad(i)
            return x

def random(sourceID='G'): #save() to be modified for reference
    link='https://api.banidb.com/v2/random/'+sourceID
    q=requests.get(link)
    r=q.json()
    x=shabad(r['shabadInfo']['shabadId'])
    return x

def banis():
    link="http://api.banidb.com/v2/banis"
    q=requests.get(link)
    r=q.json()
    d={'Bani ID':['gurmukhiUni','transliteration']}
    for i in r:
        d[i['ID']]=[]
        l=['gurmukhiUni','transliteration']
        for k in l:
            if i[k]!=None:
                d[i['ID']].append(i[k])
    return d   

def bani(baniID,larivaar=False):
    link="http://api.banidb.com/v2/banis/"+str(baniID)
    q=requests.get(link)
    r=q.json()
    d={}
    info=r['baniInfo']
    d["Info"]=[info['unicode'],info['english']]
    if info['source']['unicode'] != None:
        d["Source"]=[info['source']['unicode'],info['source']['english']]
    s=[]
    for i in r['verses']:
        b=i['verse']
        l=[b['translation']['en']['bdb']]
        if larivaar==True:
            l.insert(0,b['larivaar']['unicode'])
        else:
            l.insert(0,b['verse']['unicode'],)
        if 'bdb' in b['translation']['pu'].keys():
            l.append(b['translation']['pu']['bdb']['unicode'])
        p=[]
        for k in l:
            if k!=None and k!='':
                p.append(k)
        s.append(p)
    d['Verse']=s
    return d

def amritkeertan():
    link='http://api.banidb.com/v2/amritkeertan'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['headers']:
        l={'Header ID':i['HeaderID'],'Gurmukhi':i['GurmukhiUni'],'English':i['Transliterations']['en']}
        d.append(l)
    return d

def amritkeertanindex():
    link='http://api.banidb.com/v2/amritkeertan/index'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['index']:
        j=[]
        l=[i['HeaderID'],i['ShabadID'],i['GurmukhiUni'],i['Translations']['en']['bdb'],i['Translations']['puu']['bdb']]
        for k in l:
            if k!=None and k!='':
                j.append(k)
        d.append(j)
    return d
                

def amritkeertansearch(headerID):
    link='http://api.banidb.com/v2/amritkeertan/index/'+str(headerID)
    q=requests.get(link)
    r=q.json()
    d={}
    h=r['header'][0]
    d['Header ID']=h['HeaderID']
    d['GurmukhiUni']=h['GurmukhiUni']
    d['English']=h['Transliterations']['en']
    p=[]
    for i in r['index']:
        l=[i['ShabadID'],i['GurmukhiUni'],i['Translations']['en']['bdb'],i['SourceUnicode']]
        p.append(l)
    d['Banis']=p
    return d

def amritkeertanshabad(shabadID):
    x=shabad(shabadID)
    return x

def kosh(letter):
    link='http://api.banidb.com/v2/kosh/'+str(letter)
    q=requests.get(link)
    r=q.json()
    d=[['ਸ਼ਬਦ','Word']]
    for i in range(len(r)):
        f=r[i]
        d.append([f['wordUni'],f['word']])
    return d
        

def koshword(word):
    link='http://api.banidb.com/v2/kosh/word/'+str(word)
    q=requests.get(link)
    r=q.json()
    d=[['ਸ਼ਬਦ (Word)','ਵਿਆਖਿਆ (Definition)']]
    for i in r:
        d.append([i['wordUni'],i['definitionUni']])
    return d

def koshsearch(query):
    link='http://api.banidb.com/v2/kosh/search/'+str(query)
    q=requests.get(link)
    r=q.json()
    d=[['ਸ਼ਬਦ (Word)','ਵਿਆਖਿਆ (Definition)']]
    for i in range(len(r)):
        f=r[i]
        d.append([f['wordUni'],f['definitionUni']])
    return d

def rehats():
    link='http://api.banidb.com/v2/rehats'
    q=requests.get(link)
    r=q.json()
    d=[['Rehat ID','Rehat Name']]
    for i in r['maryadas']:
        d.append([i['rehatID'],i['rehatName']])
    return d
        

def rehat(rehatID):
    link='http://api.banidb.com/v2/rehats/'+str(rehatID)
    q=requests.get(link)
    r=q.json()
    d={'Rehat ID':rehatID,'chapters':[]}
    for i in r['chapters']:
        l={'Chapter ID':i['chapterID'],'Chapter Name':i['chapterName']}
        d['chapters'].append(l)
    return d            
    
def rehatChapter(rehatID,chapterID):
    link='http://api.banidb.com/v2/rehats/'+str(rehatID)+'/chapters/'+str(chapterID)
    q=requests.get(link)
    d=q.json()
    return d

def rehatSearch(query): #remove extra html tags from API
    link='http://api.banidb.com/v2/rehats/search/'+str(query)
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['rows']:
        l={'Rehat ID':i['rehatID'],'Chapter ID':i['chapterID'],'Chapter Name':i['chapterName']}
        d.append(l)
    return d

def writers():
    link='http://api.banidb.com/v2/writers'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['rows'][1:]:
        l={'WriterID':i['WriterID'],'WriterName':i['WriterEnglish']}
        d.append(l)
    return d

#Updated on 21/04/2021 - 16:16 IST
def raags():
    link='http://api.banidb.com/v2/raags'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['rows'][1:]:
        l={
            'Raag ID':i['RaagID'],
            'ਰਾਗ':i['RaagUnicode'],
            'Raag':i['RaagEnglish']
            }
        d.append(l)
    return d

def raag(RaagID):
    link='http://api.banidb.com/v2/raags'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['rows'][1:]:
        if i['RaagID']==RaagID:
            linkw='http://api.banidb.com/v2/writers'
            qw=requests.get(linkw)
            w=qw.json()
            s=i['SourceInfo'][0]
            op={}
            l={
                'Raag ID':i['RaagID'],
                'ਰਾਗੁ':i['RaagUnicode'],
                'Raag':i['RaagEnglish']+'\n',
                'TimeOfRaag':(i['StartTime'],i['EndTime']),
                'CommonThemes':i['CommonThemes'],
                'Feeling':i['Feeling'],
                'Angs':{s['SourceID']:[s['Start'],s['End']]},
                'Overview':i['Overview'],
                'Advanced':i['Advanced'],
                'MusicalComposure':i['MusicalComposure'],
                'Placement':i['Placement'],
                'Season':i['Season'],
                'Sargun':'',
                'Aroh':i['Sargun']['Aroh'],
                'Avroh':i['Sargun']['Avroh'],
                'Vadi':i['Sargun']['Vadi'],
                'Samvadi':i['Sargun']['Samvadi'],
                'Sur':i['Sargun']['Sur'],
                'Thaat':i['Sargun']['Thaat'],
                'Jaati':i['Jaati'],
                'Season':i['Season']
                }
            l['Writers']=[]
            for j in i['Writers']:
                for k in w['rows']:
                    if k['WriterID']==j:
                        l['Writers'].append(k['WriterEnglish']) #if writer id in writers give writer name to list
            for k in l.keys():
                if l[k]!=None and l[k]!='':
                    op[k]=l[k]
            d.append(op)
    return d


def sources():
    link='http://api.banidb.com/v2/sources'
    q=requests.get(link)
    r=q.json()
    d=[]
    for i in r['rows']:
        l={'Source ID':i['SourceID'],'SourceUni':i['SourceUnicode'],'SourceEng':i['SourceEnglish']}
        d.append(l)
    return d    

def save(dic):
    f=open('history.dat','ab')
    pickle.dump(dic,f)
    f.close()

def history(): #returns nested list of recent shabads with Shabad Id
    try:
        f=open('history.dat','rb')
        l=[]
        while True:
            try:
                x=pickle.load(f)
                l.append(x)
            except EOFError:
                break
        f.close()
        return l
    except FileNotFoundError:
        return ['No History']

def clear():
    try:
        f=open('history.dat','wb')
        f.close()
    except FileNotFoundError:
        pass