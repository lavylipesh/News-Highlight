import unittest
from models import sources,articles

class SourcesTest(unittest.TestCase):
    '''
    test class to test the behavioure of the sources objects
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_sources = Sources('')
        def test_instance(self):
            self.assertTrue(isinstance(self.new_sources.Sources))

class ArticlesTest(unittest.Testcase):
    '''
    test class to test the behaviour of the articles
    '''
    def setUp(self):
        '''
        setup method that runs before every test
        '''
        self.new_sources = Sources('')
        def test_instance(self):
            self.assertTrue(isinstance(self.new_sources.Sources))


if __name__ = '__main__':
    unittest.main()            