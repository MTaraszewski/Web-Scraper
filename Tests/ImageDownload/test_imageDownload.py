import unittest
from Webpage_class.Webpage import Webpage
from ImageDownload_class.ImageDownload import ImageDownload


class TestImageDownload(unittest.TestCase):
    def setUp(self):
        link = Webpage('http://semantive.com')
        self.image = ImageDownload(link)


class TestImageDownloadFunctions(TestImageDownload):
    def test_find_all_divs(self):
        self.assertEqual(len(self.image.find_all_divs()), 6)

    def test_find_all_divs_links(self):
        self.assertEqual(len(self.image.find_all_divs_links()), 6)

    def test_find_all_has_class_no_id_src(self):
        self.assertEqual(len(self.image.find_all_has_class_no_id_src()), 12)

    def test_img_alt_dict(self):
        self.assertEqual(len(self.image.img_alt_dict()), 12)

    def test_clean_data_get_image_links(self):
        self.assertEqual(len(self.image.clean_data_get_image_links()), 8)


if __name__ == '__main__':
    unittest.main()
