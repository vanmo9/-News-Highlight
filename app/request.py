import urllib.request,json
from .models import *

api_key = None
# Getting the base_url
base_url = None
# Getting source url



def configure_request(app):
    global api_key, base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']



def get_news(category):

    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:


        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:

            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_list):

    news_results = []

    for news_item in news_list:

        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')

        news_object = News(id,name,description,url,category)
        news_results.append(news_object)

    return news_results

def get_article(id):

    get_article_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_article_url) as url:


        get_article_data = url.read()
        get_article_response = json.loads(get_article_data)

        news_results = None

        if get_article_response['sources']:

            artrticle_results_list = get_news_response['sources']
            article_results = process_results(article_results_list)

    return article_results

def process_results(article_list):

    article_results = []

    for article_item in article_list:

        id = article_item.get('id')
        name = article_item.get('name')
        description = article_item.get('description')
        url = article_item.get('url')
        category = article_item.get('category')

        article_object = News(id,name,description,url,category)
        article_results.append(article_object)

    return article_results
