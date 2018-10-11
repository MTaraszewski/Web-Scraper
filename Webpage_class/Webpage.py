from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent


class Webpage(object):
    def __init__(self, link):
        """
        Initializes a Webpage object.

        """
        self.link = link

    def get_link(self):
        """
        Used to safely access self.link outside of the class.

        :return: self.link
        """
        return self.link

    def get_name(self):
        """
        Used to get webpage's name outside of the class.

        :return: webpage's name, if webpage's link ends with pre-defined suffix;
                 webpage's sub-page name, if webpage's link doas not end with pre-defined suffix.
        """
        suffix = ('pl', 'com', 'net')
        if self.link.endswith(suffix):
            return self.link[self.link.find("/") + 2:self.link.find(".")]
        else:
            return self.link.split('/')[-1]

    def set_request(self):
        """
        Used to set up an API method 'get', based on 'requests' library.

        :return: requests.get(self.get_link()) - API's get method request.
        """
        return requests.get(self.get_link())

    def set_request_user_agent(self):
        """
        Similar to 'set_request(self)' method, but uses 'generate_user_agent' method to simulate human behavior.

        :return: API's get method request.
        """
        user_agent = generate_user_agent(os=('mac', 'linux', 'win'))
        return requests.get(self.get_link(), headers={'user-agent': user_agent})

    def get_soup(self):
        """
        Prepares a 'soup' - a BeautifulSoup object with interacts with webpage
        and lets to fetch webpage coding for future operations.

        :return: BeautifulSoup object
        """
        return BeautifulSoup(self.set_request().text, features="html.parser")

    def __str__(self):
        """
        Allows to print an instance of a Webpage class.

        :return: str(self.link)
        """
        return str(self.link)
