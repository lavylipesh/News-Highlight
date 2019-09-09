from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_the_sources,get_sources,search_sources

@main.route('/')
def index():
    '''
    View root page function that returns the index page and it data
    '''
    
    title = 'Home - Welcome'
    general_news = get_sources("sources")
    return render_template('index.html',general=general_news)
@main.route('/articles/<articles_id>')
def articles(articles_id):
    '''
    View articles page function that returns the articles details page and its data
    '''
    sports_articles = get_articles("sports")
    return render_template('articles.html',sports = sports_articles)
@main.route('/movie/<int:id>')
def getSource(id):

    '''
    View sources page function that returns the source details page and its data
    '''
    sources = get_the_sources(id)
    title = f'{sources.title}'

    return render_template('news.html',title = title,sources = sources)
@main.route('/search/<sources_category>') 
def search(sources_category):
    '''
    view function to display the search results
    '''
    sources_category_list = sources.category.split("")
    sources_category_format = "+".join(sources_category_list)
    searched_sources = search_sources(sources_category_format)
    title = f'search results for{sources_category}'
    return render_template('serarch.html',sources = searched_sources)
   
