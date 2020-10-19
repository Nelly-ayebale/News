import urllib.request,json
from .models import News, Articles

apiKey = None
news_url = None
article_url = None

def configure_request(app):
    global apiKey, news_url,article_url
    apiKey = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_SOURCE_BASE_URL']
    article_url = app.config['NEWS_ARTICLE_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to the url request
    '''
    get_news_url = news_url.format(category,apiKey)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
    return news_results

def process_results(news_list):
    '''
    Function that processes the news_result and returns a list of objects
    '''

    news_results=[]
    for news_item in news_list:
        id = news_item.get('id')
        name= news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        country = news_item.get('country')

        news_object= News(id,name,description, url, category, country)
        news_results.append(news_object)
    
    return news_results

def get_articles(source_id):
    '''
    Function that gets the json response to the url request
    '''
    get_articles_url = article_url.format(source_id,apiKey)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    return articles_results

def process_articles(article_list):
    '''
    Function that processes the articles_results and returns a list of objects
    '''
    articles_results = []
    for article_item in article_list:
        source = article_item.get('source')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url= article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        content = article_item.get('content')

        articles_object = Articles(source, author,title,description, url, urlToImage, publishedAt, content)
        articles_results.append(articles_object)
    return articles_results