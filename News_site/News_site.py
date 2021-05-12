from flask import Flask, render_template
from newsapi.newsapi_client import NewsApiClient

url_business,url_entertainment,url_general,url_health = [],[],[],[]
news_business,news_entertainment,news_general,news_health = [],[],[],[]
img_business,img_entertainment,img_general,img_health = [],[],[],[]

newsapi = NewsApiClient(api_key="6f4af371925b421e9cf06c0edb42baf8")
topheadlines_business = newsapi.get_top_headlines(category='business', language = None, country='jp')
topheadlines_entertainment = newsapi.get_top_headlines(category='entertainment', language = None, country='jp')
topheadlines_general = newsapi.get_top_headlines(category='general', language = None, country='jp')
topheadlines_health = newsapi.get_top_headlines(category='health', language = None, country='jp')


articles_business = topheadlines_business['articles']
articles_entertainment = topheadlines_entertainment['articles']
articles_general = topheadlines_general['articles']
articles_health = topheadlines_health['articles']


app = Flask(__name__)

def list_count_business():
    for i in range(len(articles_business)):
        myarticles = articles_business[i]
        url_business.append(myarticles['url'])        
        news_business.append(myarticles['title'])
        img_business.append(myarticles['urlToImage'])
        if i + 1 == len(url_business):
            if 'youtube' in url_business[i] or 'google' in url_business[i]:
                news_business.pop(i)
                url_business.pop(i)
                img_business.pop(i)
            else:
                pass
        else:
            i = len(url_business)
            if 'youtube'in url_business[i-1] or 'google' in url_business[i-1]:
                news_business.pop(i-1)
                url_business.pop(i-1)
                img_business.pop(i-1)
            else:
                pass

def list_count_entertainment():
    for i in range(len(articles_entertainment)):
        myarticles = articles_entertainment[i]
        url_entertainment.append(myarticles['url'])        
        news_entertainment.append(myarticles['title'])
        img_entertainment.append(myarticles['urlToImage']) 
        if i + 1 == len(url_health):
            if 'youtube' in url_entertainment[i] or 'google' in url_entertainment[i]:
                news_entertainment.pop(i)
                url_entertainment.pop(i)
                img_entertainment.pop(i)
            else:
                pass
        else:
            i = len(url_entertainment)
            if 'youtube'in url_entertainment[i-1] or 'google' in url_entertainment[i-1]:
                news_entertainment.pop(i-1)
                url_entertainment.pop(i-1)
                img_entertainment.pop(i-1)
            else:
                pass

def list_count_general():
    for i in range(len(articles_general)):
        myarticles = articles_general[i]
        url_general.append(myarticles['url'])        
        news_general.append(myarticles['title'])
        img_general.append(myarticles['urlToImage']) 
        if i + 1 == len(url_health):
            if 'youtube' in url_general[i] or 'google' in url_general[i]:
                news_general.pop(i)
                url_general.pop(i)
                img_general.pop(i)
            else:
                pass
        else:
            i = len(url_general)
            if 'youtube'in url_general[i-1] or 'google' in url_general[i-1]:
                news_general.pop(i-1)
                url_general.pop(i-1)
                img_general.pop(i-1)
            else:
                pass

def list_count_health():
    for i in range(len(articles_health)):
        myarticles = articles_health[i]
        url_health.append(myarticles['url'])        
        news_health.append(myarticles['title'])
        img_health.append(myarticles['urlToImage']) 
        if i + 1 == len(url_health):
            if 'youtube' in url_health[i] or 'google' in url_health[i]:
                news_health.pop(i)
                url_health.pop(i)
                img_health.pop(i)
            else:
                pass
        else:
            i = len(url_health)
            if 'youtube'in url_health[i-1] or 'google' in url_health[i-1]:
                news_health.pop(i-1)
                url_health.pop(i-1)
                img_health.pop(i-1)
            else:
                pass

@app.route('/')
def index():
    list_count_business()
    list_count_entertainment()
    list_count_general()
    list_count_health()
    mylist_business = zip(news_business, url_business, img_business)
    mylist_entertainment = zip(news_entertainment, url_entertainment, img_entertainment)
    mylist_general = zip(news_general, url_general, img_general)
    mylist_health = zip(news_health, url_health, img_health)
    return render_template('index.html',text_business=news_business,text_entertainment=news_entertainment,text_general=news_general,text_health=news_health,image_business=img_business,image_entertainment=img_entertainment,image_general=img_general,image_health=img_health,link_business=url_business,link_entertainment=url_entertainment,link_general=url_general,link_health=url_health,context_business=mylist_business,context_entertainment=mylist_entertainment,context_general=mylist_general,context=mylist_health) # tempaltesフォルダのhtmlファイルを返している

if __name__ == '__main__':
    app.run()
