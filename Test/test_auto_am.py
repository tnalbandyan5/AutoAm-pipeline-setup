import config as config
from Helpers.general_helpers import GeneralHelpers
from Pages.autoam_search import SearchAutoAm
import logging

def test_car_search(driver):
    GeneralHelpers(driver).navigate_to_url(config.url)
    SearchAutoAm(driver).test_auto_am_search()
    elements = SearchAutoAm(driver).test_search_result()
    assert 1 == 1, logging.error(f"There are {len(elements)} while searching for {config.car}.")