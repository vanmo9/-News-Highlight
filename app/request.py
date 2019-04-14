from app import app
import urllib.request,json
from .models import news

News = news.News


# Getting api key
api_key = app.config['NEWS_API_KEY']


# Getting the news base url
base_url = app.config["news url"]



def get_news(id):
    get_news_details_url = base_url.format(id,api_key)

    with  urllib.request.urlopen(get_news_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(news_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            overview = news_details_response.get('overview')
            poster = news_details_response.get('poster_path')
            vote_average = news_details_response.get('vote_average')
            vote_count = news_details_response.get('vote_count')


            news_object = News(id,title,overview,poster,vote_average,vote_count)


    return news_object



def get_news(category):
    '''
    function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(category,api_key)


    with urllib.request.urlopen(get_newss_url) as url:
        get_newss_data = url.read()
        get_newss_responce = json.loads(get_newss_data)


        news_results = None


        if get_newss_responce['results']:
            news_results_list = get_newss_responce['results']
            news_results = process_results(news_results_list)


    return news_results


def proccess_results(news_list):
    '''
    function that proccess the news result and transform them to alist of objects

    Args:
        news_list: a list of dictionaries that contain news details


    returns:
        news_results: a list of news objects
    '''
    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        title = news_item.get('original_title')
        overview = news_item.get('overview')
        poster = news_item.get('paoster_path')
        vote_average = news_item.get('vote_average')
        vote_count = news_item.get('vote_count')


        if poster:
            news_object = News(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results


def search_news(news_name):
    search_news_url = ''
    with urllib.request.urlopen(search_news_url) as url:
        search_news_data = url.read()
        search_news_response = json.loads(search_news_data)

        search_news_results = None

        if search_news_response['results']
            search_news_list = search_news_response['results']
            search_news_results = process_results(search_news_list)


    return search_news_results            
