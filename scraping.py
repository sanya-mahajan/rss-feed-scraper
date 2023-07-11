import requests,json
from bs4 import BeautifulSoup
url='https://news.ycombinator.com/rss'


def hackernews_rss(url):
    try:
        r=requests.get(url)
        soup=BeautifulSoup(r.content,features='xml')
        articles=soup.findAll('item')
        articlelist=[]
        for a in articles:
            title= a.find('title').text
            link= a.find('link').text
            pubDate= a.find('pubDate').text
            articles={title,link,pubDate}
            articlelist.append(articles)
        return save_to_file(articlelist)    
    except Exception as e:
        return print('failed',e)
    



def save_to_file(articlelist):
    with open('hackernews.txt','w') as outfile:
        for a in articlelist:
            json.dump(list(a),outfile)

print('started scraping')    
hackernews_rss('https://news.ycombinator.com/rss')
print('finished scraping')        