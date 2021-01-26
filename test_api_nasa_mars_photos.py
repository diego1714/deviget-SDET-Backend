import unittest
import os
import configparser
import json
import response_item_data
import requests

from helpers import send_req


class TestApiNasa(unittest.TestCase):
    # Read data.cfg
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_parser = configparser.RawConfigParser()
    config_file_path = dir_path + '\\data.cfg'
    config_parser.read(config_file_path)

    def test_page_api(self):
        # Check if api return max of 25 item when use page
        # Create url request
        base_api = self.config_parser.get('nasa_photo_api', 'base_api')
        key_api = self.config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url = base_api + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = send_req(url)

        # Assert true if return 25 items
        self.assertEqual(len(resp), 25)

    def test_data_structure(self):
        # Check the item data structure
        base_api = self.config_parser.get('nasa_photo_api', 'base_api')
        key_api = self.config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url = base_api + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = send_req(url)

        data_expected = response_item_data.data
        data_received = resp[0]

        # Compare the two list // only compared de variable not the data
        list_compare = [i for i in data_received if i not in data_expected] == []

        self.assertTrue(list_compare)

    def test_invalid_key(self):
        # Check invalid key
        base_api = self.config_parser.get('nasa_photo_api', 'base_api')
        key_api = '0303456'
        time = '1000'

        url = base_api + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = requests.get(url)

        self.assertEqual(resp.status_code, 403)

    def test_invalid_url(self):
        # Check invalid url
        base_api = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/123hotos?'
        key_api = self.config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url = base_api + '&123' + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = requests.get(url)

        self.assertEqual(resp.status_code, 404)

    def test_invalid_url_rover_name(self):
        # Check send invalid rover name
        base_api = 'https://api.nasa.gov/mars-photos/api/v1/rovers/test/photos?'
        key_api = self.config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url = base_api + '&123' + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp = requests.get(url)

        self.assertEqual(resp.status_code, 400)

