import unittest
import os
import configparser
import requests
import json
from helpers import send_req, calculate_earth_time, first_ten_image


class CompareTenPhotosEarthMarsTime(unittest.TestCase):
    def test_compare_ten_photos_earth_mars_time(self):
        # Read data.cfg
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_parser = configparser.RawConfigParser()
        config_file_path = dir_path + '\\data.cfg'
        config_parser.read(config_file_path)

        # Create url request
        base_api = config_parser.get('nasa_photo_api', 'base_api')
        key_api = config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url = base_api + 'sol=' + time + '&page=1' + '&api_key=' + key_api

        # Send request
        resp_mars_time = send_req(url)

        # Retrieve the 10 first mars images
        list_image_mars = first_ten_image(resp_mars_time)

        # Check the len of the images list
        self.assertEqual(len(list_image_mars), 10)

        # Calculate the earth time
        landing_date = config_parser.get('nasa_photo_api', 'landing_date')
        # Mars time to convert
        sum_date = '1000'
        time_earth = calculate_earth_time(landing_date, sum_date)

        url_earth = base_api + 'earth_date=' + time_earth + '&page=1' + '&api_key=' + key_api

        # Send request
        resp_earth_time = send_req(url_earth)

        # Retrieve the 10 first earth images
        list_image_earth = first_ten_image(resp_earth_time)

        # Check the len of the images list
        self.assertEqual(len(list_image_earth), 10)

        # Compare the two list
        list_compare = [i for i in list_image_earth if i not in list_image_mars] == []

        self.assertTrue(list_compare)
