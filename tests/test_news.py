import unittest
from app.models import News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setup(self):
        '''
        Setup method that will run before each test
        '''
        self.new_news = News('abc', 'ABC NEWS', 'The best news worldwide', 'www.abc.com', 'general', 'UK')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))
        