from app import main
import urllib.request,json
from .models import Sources,Articles
import os

# getting api key
api_key = None

# getting base url
base_url = None
def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']

def get_sources(category):
    '''
    function that gets the json response to our url requests
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['sources']:
            sources_list = get_sources_response['sources']
            sources_results = process_sources_results(sources_list)

    return sources_results
def get_articles(id):
    '''
    function that gets the json response to our url requests
    '''
    get_articles_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        if get_articles_response['articles']:
            articles_list = get_articles_response['articles']
            articles_results = process_articles_results(articles_list)

    return articles_results
def process_sources_results(sources_list): 
    '''
    function that processes the  sources results and transform them into a list of objects
    '''
    sources_results = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        language = source_item.get('language')
        country = source_item.get('country')
        category = source_item.get('category')
        
        source_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(source_object)

    return sources_results
def process_articles_results(articles_list):
    '''
    function that processess the article result and  transform them into a list of objects
    '''
    articles_results = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item('description')
        url = article_item('url')
        urlToImage = article_item('urlToImage')
        publishedAt = article_item('publishedAt')
        content = article_item('content')

        article_object = Articles(id,author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(article_object)
    
    return articles_results

