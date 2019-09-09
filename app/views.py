from flask import render_template
from app import app
from .requests import get_the_sources,get_sources

@app.route('/')
def index():
    '''
    View root page function that returns the index page and it data
    '''
    
    title = 'Home - Welcome'
    return render_template('index.html')
@app.route('/sources/<sources_id>')
def sources(sources_id):
    '''
    View sources page function that returns the sources details page and its data
    '''
    general_news = get_sources("general")
    return render_template('sources.html',general=general_news)
@app.route('/articles/<articles_id>')
def articles(articles_id):
    '''
    View articles page function that returns the articles details page and its data
    '''
    sports_articles = get_articles("sports")
    return render_template('articles.html',sports = sports_articles)
@app.route('/movie/<int:id>')
def getSource(id):

    '''
    View sources page function that returns the source details page and its data
    '''
    sources = get_the_sources(id)
    title = f'{sources.title}'

    return render_template('news.html',title = title,sources = sources)    
