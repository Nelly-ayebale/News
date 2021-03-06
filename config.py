import os

class Config:

    NEWS_SOURCE_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    NEWS_ARTICLE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'
    


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}