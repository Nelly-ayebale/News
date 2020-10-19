import urllib.request,json
from .models import News

apiKey = None
news_url = None

def configure_request(app):
    global apiKey, news_url
    apiKey = app.config['NEWS_API_KEY']
    news_url = app.config['NEWS_SOURCE_BASE_URL']

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
    Function that processes the news_result anf returns a list of objects
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