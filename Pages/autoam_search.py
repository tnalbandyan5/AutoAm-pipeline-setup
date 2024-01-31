from Helpers.general_helpers import GeneralHelpers
from selenium.webdriver.common.by import By
import config as config

class SearchAutoAm(GeneralHelpers):

    search_field = (By.XPATH, "//input[@id='searchInp']")
    # search_button = (By.XPATH, "//input[@id='submit_search-small']")
    research_div = (By.XPATH, "//div[@class='card ']")
    possible_options = (By.XPATH, "//p[@class='inactiveAC']")

    def test_auto_am_search(self):
        try:
            self.find_and_send_keys(self.search_field, config.car)
            # self.find_and_click(self.search_button)
            self.find_and_click(self.possible_options)
        except Exception as e:
            print(f"something went wrong while searching for car - {e}")

    def test_search_result(self):
        try:
            result = self.find_elem_in_ui(self.research_div)
            return result
        except Exception as e:
            print(f"something went wrong in search result page - {e}")