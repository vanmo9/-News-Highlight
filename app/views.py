from flask import render_template
from app import app
from .request import get_newss,get_news

## Views
@app.route('/')
def index():
    '''

    View root page function that returns the index page and its data
    '''

    # Getting popular news highlights
    popular_newss = get_newss('popular')
    upcoming_news = get_newss('upcoming')
    now_showing_news = get_newss('now_showing_news')
    title = 'python the language'
    return render_template('index.html', title = title,popular = popular_newss,  upcoming = upcoming_news, now_showing = now_showing_news)




@app.route('/news/<int:id>')
def news(id):

    '''
    this is view function that returns the news details page and its data
    '''

    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html', title = title, news = news)
