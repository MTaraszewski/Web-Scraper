import unittest
from Webpage_class.Webpage import Webpage
from TextDownload_class.TextDownload import TextDownload


class TestTextDownload(unittest.TestCase):
    def setUp(self):
        link = Webpage('http://semantive.com')
        self.text = TextDownload(link)


class TestTextDownloadFunctions(TestTextDownload):
    def test_prepare_body(self):
        self.assertEqual(len(self.text.prepare_body()), 9)

    def test_filter_body(self):
        self.assertEqual(len(self.text.filter_body()), 40)

    def test_list_to_dict(self):
        self.assertEqual(len(self.text.list_to_dict()), 40)


if __name__ == '__main__':
    unittest.main()
