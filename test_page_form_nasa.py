import unittest
import os
import configparser

from selenium import webdriver
from selenium.webdriver.common.by import By
from locator_page import HomePageLocators


class PageFormNasa(unittest.TestCase):
    def setUp(self):
        # Create a new Chrome session
        # Download the same chromedriver version that you chrome browser
        # https://chromedriver.storage.googleapis.com/index.html
        # Modified the location file
        self.driver = webdriver.Chrome('C:/Users/diego/Downloads/chromedriver')
        # Read data.cfg
        self.dir_path = os.path.dirname(os.path.realpath(__file__))
        self.config_parser = configparser.RawConfigParser()
        self.config_file_path = self.dir_path + '\\data.cfg'
        self.config_parser.read(self.config_file_path)

        # Go to nasa url
        nasa_url = self.config_parser.get('nasa_photo_api', 'nasa_web_page')
        self.driver.get(nasa_url)

    def test_form(self):
        # Test the NASA form page
        first_name = self.config_parser.get('nasa_photo_api', 'first_name')
        last_name = self.config_parser.get('nasa_photo_api', 'last_name')
        email = self.config_parser.get('nasa_photo_api', 'email')

        # Find the form first name and a send name
        form_first_name = self.driver.find_element(By.XPATH, HomePageLocators.first_name)
        form_first_name.send_keys(first_name)

        # Find the form last name and send a last name
        form_last_name = self.driver.find_element(By.XPATH, HomePageLocators.last_name)
        form_last_name.send_keys(last_name)

        # Find the form email and send a email
        form_email = self.driver.find_element(By.XPATH, HomePageLocators.email)
        form_email.send_keys(email)

        # Click signup button
        self.driver.find_element(By.XPATH, HomePageLocators.signup_button).click()
        self.driver.implicitly_wait(10)

        # Check the response of the web page
        # Check the response email
        email_resp = self.driver.find_element(By.XPATH, "//strong[contains(text(),'" + email + "')]").text
        self.assertEqual(email, email_resp)

        # Check the key code response is not empty
        key_resp = self.driver.find_element(By.XPATH, HomePageLocators.key_response).text
        self.assertTrue(key_resp)

        # Check the https example response
        https_example = self.driver.find_element(By.XPATH, HomePageLocators.https_response).text
        self.assertTrue(https_example)

    def end_test(self):
        self.driver.quit()
