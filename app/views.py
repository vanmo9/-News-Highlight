from flask import render_template,request,redirect,url_for
from app import app
from .request import get_newss,get_news,search_news
from .models import review
from .forms import ReviewForm
Review = review.Review

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

    search_news = request.args.get('news_query')

    if search_news:
        return redirect(url_for('search',news_name=search_news))
    else:
        return render_template('index.html', title = title,popular = popular_newss,  upcoming = upcoming_news, now_showing = now_showing_news)




@app.route('/news/<int:id>')
def news(id):

    '''
    this is view function that returns the news details page and its data
    '''

    news = get_news(id)
    title = f'{news.title}'

    return render_template('news.html', title = title, news = news)


@app.route('/search/<news_name>')
def search(news_name):
    '''
    view function that displays search results
    '''

    news_name_list = news_name.spilt("")
    news_name_format = "+".json(news_name_list)
    search_news = search_news(search_news_format)
    title = f'search results for {news_name}'
    return render_template('search.html',news = searched_news)



@app.route('/news/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    news = get_news(id)


    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(news.id,title,news.poster,review)
        new_review.save_review()
        return redirect(url_for('news',id = news.id ))

    title = f'{news.title} review'
    return render_template('new_review.html',title = title, review_form=form, news=news)
    
