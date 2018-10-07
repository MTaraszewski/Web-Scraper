#####################################################
##
## AUTHOR: MTaraszewski
##
## OBJECTIVE: Provide Web Scraping tool Image Download class
##
#####################################################

###########################################################
## STEP 0: LIBRARIES
###########################################################

from Webpage_class.Webpage import Webpage
from multiprocessing import Pool
import urllib.request

###########################################################
## STEP 1 HELPER FUNCTIONS DEFINITION
###########################################################


def has_class_but_no_id_src(tag):
    """
    A function that returns True if a tag defines the “class” attribute but doesn’t define the “id” attribute.
    :param tag: webpage coding tag within the 'soup'

    :return: tags with 'src' and w/o 'id' attributes
    """
    return tag.has_attr('src') and not tag.has_attr('id')

###########################################################
## STEP 2 CLASS(ES) DEFINITION
###########################################################


class ImageDownload(Webpage):
    def __init__(self, input_object):
        """
        Initializes a ImageDownload object.

        :param input_object: an object from which data will be fetched.

        A ImageDownload object has one attribute:
            self.input_object (an instance of Webpage class)
        """
        self.input_object = input_object

    def find_all_divs(self):
        """
        Finds all 'divisions' ('div') tags of parameters {'class': 'box-bg'} within the 'soup'

        :return: 'soup' with only 'divisions' tags of parameters {'class': 'box-bg'}
        """
        return self.input_object.get_soup().find_all('div', {'class': 'box-bg'})

    def find_all_divs_links(self):
        """
        Returns a dictionary of image links, based on all 'divisions' with 'class' type: 'box-bg'

        Args:
            input_list (list): The only parameter.

        :return: conatiner (dictionary): A dictionary of image links, where keys = 0,...,n (ints of range n)
        and values = corresponding links.
        """
        filtered_soup = self.find_all_divs()
        container = {}
        for item in range(len(filtered_soup)):
            item_cleaned = filtered_soup[item].get('style')
            container[item] = item_cleaned[
                              item_cleaned.find("'") + 1:item_cleaned.find("'", item_cleaned.find("'") + 1)]
        return container

    def find_all_has_class_no_id_src(self):
        """
        Returns a 'soup' with “class” attribute but w/o the “id” attribute within the 'soup'

        :return: 'soup' with “class” and w/o the “id” attributes
        """
        return self.input_object.get_soup().find_all(has_class_but_no_id_src)

    def img_alt_dict(self):
        """
        Returns dictionary based on 'find_all_has_class_no_id_src' method content
        and with 'img alt' tag with 'src' attribute within the 'soup'

        :return: img_alt_dict (dictionary)
        """
        filtered_soup =  self.find_all_has_class_no_id_src()
        img_alt_dict = {}
        for i in range(len(filtered_soup)):
            img_alt_dict[i] = filtered_soup[i].get('src')
        return img_alt_dict

    def clean_data_get_image_links(self):
        """
        Cleans/filters 'soup' based on 'img_alt_dict' method content and pre-defined image types of interest.

        :return: output_dict (dictionary)
        """
        image_types_list = ['png', 'jpeg', 'jpg', 'svg']
        input_dict = self.img_alt_dict()
        output_dict = {}
        counter = 0
        for item in range(len(input_dict)):
            if input_dict[item][input_dict[item].rfind(".") + 1:] in image_types_list:
                output_dict[counter] = input_dict[item]
                counter += 1
        return output_dict

    def download_images(self, input_dict):
        """
        Downloads images based on provided dictionary

        Args:
            input_dict (dict): The only parameter.

        :return: All images in input_dict saved into chosen directory.
        """
        for e in list(input_dict.keys()):
            urllib.request.urlretrieve(str(input_dict[e]), str(input_dict[e].split('/')[-1]))

    def download_function(self, arg1):
        """
        A function that uses 'urllib.request' library and its 'urlretrieve' method to download image
        based on provided link(arg1). Also saves file with its original name.

        :param arg1: an image link
        :return: downloads image based on provided link
        """
        return urllib.request.urlretrieve(arg1, arg1.split('/')[-1])

    def download_images_with_pool(self, input_dict):
        """
        Employees 'Pool' method from 'multiprocessing' library for parallel processing tasks

        :param input_dict: a dictionary with images links
        :return: my_pool.map(self.download_function, my_data_list)
        """
        my_pool = Pool()
        my_data_list = list(input_dict.values())
        return my_pool.map(self.download_function, my_data_list)
