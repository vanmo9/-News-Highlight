import unittest
from models import news
News = news.News


class NewsTest(unittest.TestCase):
    '''
    test class that tests the behaviour of the movie class
    '''

    def setUp(self):
        '''
        set up method that will run before every test
        '''
        self.new_news = News(1234,python )

    def test_instances(self):
        self.assertTrue(isintance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()
