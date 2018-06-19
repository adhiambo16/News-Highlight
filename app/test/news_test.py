import unittest
from models import news

Source = news.Source


class NewsTest(unittest.TestCase):
    def setUp(self):
        '''Set up method that will run before every Test'''
        self.new_news = Source('axios', 'Axios', 'Axios are a new media company',
                               'www.axios.com', 'general', 'en', 'gb')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, Source))


if __name__ == '__main__':
    unittest.main()
