import requests
import os
import errno

PATH = os.path.dirname(os.path.realpath(__file__))


def get_link():
    """
    Takes webpage link provided by user and returns it.

    :return: string
    """
    msg = 'Write a webpage link(should start with ("http://" or "https://") ' \
          'and end with appropriate domain(e.g. ".com"): '
    return input("{}".format(msg))


def check_link(input_link):
    """
    Checks whether provided link has proper both prefix and suffix
    :param input_link: string
    :return:    True - if link meets prefix and suffix criteria
                False - otherwise
    """
    prefix = ('http', 'https')
    suffix = ('pl', 'com', 'net', 'team', 'case-studies', 'career', '404')
    input_link = input_link.lower()
    if (input_link.startswith(prefix)) and (input_link.endswith(suffix)):
        return True
    else:
        print("\nThe value error is: {}\nThe link specified is: {}. "
              "Please correct input. \n".format('Invalid link', input_link))
        return False


def start_scraping(class_type):
    """
    Initiate scraping. Reads webpage link, tests it and if correct, returns instance of Webpage class.

    :param class_type: call class type

    :return: An instance of called class (Webpage should be called).
    """
    while True:
        try:
            read_input = input('Enter "n" to start a new scraping or "e" to end game: ')
            print('')
            read_input_lower = read_input.lower()
            if read_input_lower == 'e':
                break
            if read_input_lower == 'n':
                link = get_link()
                if check_link(link):
                    return class_type(link)
            if read_input_lower not in 'en':
                print('Invalid letter')
        except ValueError:
            print('Invalid command')


def check_connection(input_object):
    """
    Checks connection status.

    :param input_object: an instance of Webpage class

    :return: Prints connection status. Returns boolean.
    """
    if input_object.set_request().status_code == requests.codes.ok:
        print('Connection status: OK')
        return True
    else:
        if input_object.set_request_user_agent().status_code == requests.codes.ok:
            print('Connection status: OK')
            return True
        else:
            print('Connection failed - try other methods to set connection\n')
            input_object.set_request_user_agent().raise_for_status()
            return False


def create_folder(link_name):
    folder_name = link_name.get_name()
    try:
        os.makedirs(folder_name)
        print('Folder successfully created')
    except OSError as e:
        if e.errno == errno.EEXIST:
            print('Folder already exists and operation abandoned')
            raise


def change_directory(link_name):
    new_path = os.path.join(PATH, link_name.get_name())
    os.chdir(new_path)
    print('Directory changed')
