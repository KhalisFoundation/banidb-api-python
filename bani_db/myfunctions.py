import requests

def run(link):
    q=requests.get(link)
    r=q.json()
    for j in r['verses']:
        print('Shabad Id: ',j['shabadId'])
        print(j['verse']['unicode'])
        print(j['translation']['en']['bdb'])
        print(j['translation']['pu']['bdb']['unicode'])
        print(j['source']['english'],'-',j['source']['pageNo'],',',j['writer']['english'],j['raag']['english'])
        print('\n')
    return r
def search(query,searchtype=1,source='all',ang=None,raag=None,writer=None,page=1,results=None):
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
        res+=i+str(s[i])+'&'
    response=requests.get(res)
    result=response.json()
    info=result['resultsInfo']
    totalRes=info['totalResults'] #Total Shabads found!
    totalPages=info['pages']['totalPages'] #Total Pages
    for k in range(1,totalPages+1):
        info=result['resultsInfo']
        print('Search results for Page ',k)
        result=run(res)
        if 'nextPage' in info['pages'].keys():
            res=info['pages']['nextPage']
    