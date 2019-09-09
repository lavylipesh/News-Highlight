from app import app
import urllib.request,json
from .models import sources,articles

# getting api key
api_key = app.config['NEWS_API_KEY']

# getting base url
base_url = app.config["NEWS_API_BASE_URL"]

def get_sources(category):
    '''
    function that gets the json response to our url requests
    '''
    get_sources_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        sources_results = None
        if get_sources_response['results']:
            sources_list = get_sources_response['results']
            sources_results = process_sources_results(sources_list)
def get_articles(category):
    '''
    function that gets the json response to our url requests
    '''
    get_articles_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        articles_results = None
        if get_artiicles_response['results']:
            articles_list = get_articles_response['results']
            articles_results = process_articles_results(articles_list)
def process_sources_results(sources_list): 
    '''
    function that processes the  sources results and transform them into a list of objects
    '''
    sources_results = []
    for source_item in sources_list:
        source_object = Source(*source_item.values())
        sources_results.append(source_object)

    return sources_results
def process_articles_results():
    '''
    function that processess the article result and  transform them into a list of objects
    '''
    articles_results = []
    for article_item in articles_list:
        if article_item['urlToImage']:
            article_object = Article(*article_item.values())
            articles_results.append(article_object)
    return articles_results
def get_the_sources(id):
    get_sources_details_url = base_url.format(id,api_key)
    with urllib.request.urlopen(get_sources_details_url)
as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        source_results = None

        if get_sources_response['articles']:
            sources_list = get_sources_response['articles']
            sources_results = process_results(sources_list)
    return sources_results
