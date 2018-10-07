import unittest
from Webpage_class.Webpage import Webpage


class TestWebpage(unittest.TestCase):
    def setUp(self):
        self.webpage = Webpage('http://semantive.com')


class TestWebpageFunctions(TestWebpage):
    def test_get_link(self):
        self.assertEqual(self.webpage.get_link(), 'http://semantive.com')

    def test_get_name(self):
        self.assertEqual(self.webpage.get_name(), 'semantive')
        self.assertNotEqual(self.webpage.get_name(), 'team')

    def test_set_request(self):
        self.assertEqual(str(self.webpage.set_request()), '<Response [200]>')

    def test_set_request_user_agent(self):
        self.assertEqual(str(self.webpage.set_request_user_agent()), '<Response [200]>')

    def test_get_soup(self):
        self.assertEqual(len(self.webpage.get_soup()), 71)


if __name__ == '__main__':
    unittest.main()
