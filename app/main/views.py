from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news

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

