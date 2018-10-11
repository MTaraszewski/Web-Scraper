from Webpage_class.Webpage import Webpage


class TextDownload(Webpage):
    def __init__(self, input_object):
        """
        Initializes a TextDownload object.
        """
        self.input_object = input_object

    def prepare_body(self):
        """
        Prepares and returns 'body' of a 'soup'

        :return: self.input_object.get_soup().body
        """
        return self.input_object.get_soup().body

    def filter_body(self):
        """
        Filters prepared 'body' (prepare_body(self) method) with provided tags.

        :return: List of coding objects of provided tags.
        """
        headers = ['h1', 'h2','h3','h4','h5','h6','p']
        return list(self.prepare_body().find_all(headers))

    def list_to_dict(self):
        """
        Changes a list to a dictionary.

        :return: list of a 'filter_body()' method objects
        """
        temp_list = self.filter_body()
        temp_dict = {}
        for item in range(len(temp_list)):
            temp_dict[item] = temp_list[item]
        return temp_dict

    def write_to_file(self):
        """
        Writes to file filtered text from 'soup'.

        :return: A file in specified folder.
        """
        file_name = self.input_object.get_name()
        print('Creating a file named: {}, and writing there text data.'.format(file_name))
        with open("{}".format(file_name)+'.txt', 'w') as file:
            file.write(str(self.list_to_dict()))
            print('File: {}, successfully created, saved and closed.'.format(file_name))
