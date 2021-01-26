import unittest
import os
import configparser
import requests
import json
from helpers import send_req, compare_list


class CompareCameraAmountsPictures(unittest.TestCase):

    def test_compare_amount_photos(self):
        # Read data.cfg
        dir_path = os.path.dirname(os.path.realpath(__file__))
        config_parser = configparser.RawConfigParser()
        config_file_path = dir_path + '\\data.cfg'
        config_parser.read(config_file_path)

        # Create urls request for each camera
        base_api = config_parser.get('nasa_photo_api', 'base_api')
        key_api = config_parser.get('nasa_photo_api', 'key_api')
        time = '1000'

        url_fhaz = base_api + 'sol=' + time + '&camera=' + 'fhaz' + '&api_key=' + key_api
        url_rhaz = base_api + 'sol=' + time + '&camera=' + 'rhaz' + '&api_key=' + key_api
        url_mast = base_api + 'sol=' + time + '&camera=' + 'mast' + '&api_key=' + key_api
        url_chemcam = base_api + 'sol=' + time + '&camera=' + 'chemcam' + '&api_key=' + key_api
        url_mahli = base_api + 'sol=' + time + '&camera=' + 'mahli' + '&api_key=' + key_api
        url_mardi = base_api + 'sol=' + time + '&camera=' + 'mardi' + '&api_key=' + key_api
        url_navca = base_api + 'sol=' + time + '&camera=' + 'navca' + '&api_key=' + key_api

        # Send requests for each camera
        fhaz_camera = send_req(url_fhaz)
        rhaz_camera = send_req(url_rhaz)
        mast_camera = send_req(url_mast)
        chemcam_camera = send_req(url_chemcam)
        mahli_camera = send_req(url_mahli)
        mardi_camera = send_req(url_mardi)
        navcam_camera = send_req(url_navca)

        # Compare the amounts of pictures
        # compare_list = Returns true, if the maximum number of photos is less than 10 times the minimum
        result = compare_list(len(fhaz_camera), len(rhaz_camera), len(mast_camera), len(chemcam_camera), len(mahli_camera),
                     len(mardi_camera), len(navcam_camera))

        self.assertTrue(result)

