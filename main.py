from helper_functions import *
from Webpage_class.Webpage import Webpage
from ImageDownload_class.ImageDownload import ImageDownload
from TextDownload_class.TextDownload import TextDownload
import sys

if __name__ == '__main__':
    ##    START    ##
    print("----------------------------------------------------------------------")
    print('\nStarting Scraper\n')
    print("----------------------------------------------------------------------")
    webpage_link = start_scraping(Webpage)
    print("----------------------------------------------------------------------")

    ## CHECK CONNECTION ##

    print('Testing connection...')
    if check_connection(webpage_link) != True:
        sys.exit()
    else:
        pass
    print("----------------------------------------------------------------------")

    ## CREATE NEW FOLDER AND SET A NEW PATH ##

    print('Creating new folder...')
    create_folder(webpage_link)
    print("----------------------------------------------------------------------")
    print('Change directory...')
    change_directory(webpage_link)
    print("----------------------------------------------------------------------")

    ## DOWNLOAD IMAGES ##

    class_image_download_object = ImageDownload(webpage_link)
    print('Start downloading images...\n')
    print('First group of images downloading...')
    class_image_download_object.download_images_with_pool(class_image_download_object.find_all_divs_links())
    print('Downloading status: SUCCESS')
    print("----------------------------------------------------------------------")
    print('Second group of images downloading...')
    class_image_download_object.download_images_with_pool(class_image_download_object.clean_data_get_image_links())
    print('Downloading status: SUCCESS')
    print("----------------------------------------------------------------------")

    ## DOWNLOAD TEXT ##

    class_text_download_object = TextDownload(webpage_link)
    print('Start downloading text...\n')
    class_text_download_object.write_to_file()
    print('Downloading status: SUCCESS')
    print("----------------------------------------------------------------------")

    ## END OF SCRAPER ##

    print('Scraping images and text went successfully.\nThank you for spending time with us. Hope you have enjoyed.')
