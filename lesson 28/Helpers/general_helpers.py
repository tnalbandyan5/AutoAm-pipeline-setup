import logging
import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class GeneralHelpers:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_url(self, url):
        try:
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.set_page_load_timeout(20)
            logging.info(f"Navigated to URL: '{url}'")
        except Exception as e:
            logging.error(f"Error navigating to URL: '{url}'. {e}")
            raise


    def find_and_click(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10).until(EC.visibility_of_all_elements_located(locator))
            elem = self.driver.find_element(*locator)
            logging.info(f"Possible options are found.")
            elem.click()
            logging.info(f"1st option is clicked on.")
        except Exception as e:
            logging.error(f"Error finding element {locator} or clicking: {e}")
            raise

    def find_and_send_keys(self, locator, text):
        try:
            elem = self.driver.find_element(*locator)
            logging.info(f"Search field is found.")
            elem.click()
            elem.clear()
            elem.send_keys(text)
            logging.info(f"'{text}' is typed in Search field.")
        except Exception as e:
            logging.error(f"Error finding element {locator} or sending keys: {e}")
            raise
    
    def find_elem_in_ui(self, locator):
        try:
            elements = self.driver.find_elements(*locator)
            logging.info(f"{len(elements)} elements are found.")
            return elements
        except Exception as e:
            logging.error(f"Error finding element {locator} or waiting for presence: {e}")
            return elements
