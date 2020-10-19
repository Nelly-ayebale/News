from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news, get_articles

@main.route('/')
def index():
    '''
    Function that returns the index page and it's data
    '''

    gen_news = get_news('general')
    tech_news = get_news('technology')
    bus_news = get_news('business')
    ent_news = get_news('entertainment')
    sport_news = get_news('sports')

    title = "Welcome to your news"

    return render_template('index.html', title = title, general = gen_news, technology = tech_news, business= bus_news, entertainment = ent_news, sports = sport_news)



@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns the articles page and it's data
    '''
    title = f'{source_id}'
    articles_return = get_articles(source_id)
    return render_template('articles.html', title = title, articles = articles_return)