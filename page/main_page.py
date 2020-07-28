from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):
    _search_locator = (By.ID, "com.hexin.plat.android:id/tips")

    def to_search(self):
        sleep(3)
        #todo: too slow
        self.find_element_and_click(self._search_locator)
        return SearchPage(self.driver)