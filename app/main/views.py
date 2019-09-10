from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_articles

@main.route('/')
def index():
    '''
    View root page function that returns the index page and it data
    '''
    
    title = 'Home - Welcome'
    general_news = get_sources("sources")
    return render_template('index.html',general=general_news)
@main.route('/articles/<articles_id>')
def news(id):
    '''
    View articles page function that returns the articles details page and its data
    '''
    news = get_articles("id")
    return render_template('news.html',all = all_articles)
@main.route('/sources/<int:id>')
def getSource(id):

    '''
    View sources page function that returns the source details page and its data
    '''
    sources = get_sources(id)
    title = f'{sources.title}'

    return render_template('news.html',title = title,sources = sources)

