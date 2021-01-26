import unittest
import os
import configparser
import json
from helpers import send_req, first_ten_image


class TenFirstPhotosCuriosityMartianTime(unittest.TestCase):

    def test_ten_first_photos_curiosity_martian_time(self):

        # Read data.cfg
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_parser = configparser.RawConfigParser()
        config_file_path = dir_path + '\\data.cfg'
        config_parser.read(config_file_path)

        # Create url request
        base_api = config_parser.get('nasa_photo_api', 'base_api')
        key_api = config_parser.get('nasa_photo_api', 'key_api')
        # Mars Time
        time = '1000'

        url = base_api + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = send_req(url)

        # Retrieve the 10 first images
        list_image = first_ten_image(resp)

        # Check the len of the images list
        self.assertEqual(len(list_image), 10)

