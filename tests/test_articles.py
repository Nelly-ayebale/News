import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setup(self):
        '''
        Setup method that will run before each test
        '''
        self.new_article = Articles('abc', 'Nelly', 'An Old woman dies after getting the Corona Virus', 'This woman was admitted on a rush', 'kkndndkndk', 'njcncjnjce', 'Monday,19th October,2020', 'The hospital confirmed that the area she lived in had more residents with the virus')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
        