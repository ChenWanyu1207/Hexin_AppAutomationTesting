from selenium.webdriver.common.by import By
from page.base_page import BasePage


class SearchPage(BasePage):
    _input_locator = (By.ID, "com.hexin.plat.android:id/search_input")
    _join_or_delete_locator = (By.ID, "is_self_code")
    _toast_or_delete_locator = (By.ID, "tv_toast_content")

    def search(self, keyword):
        self.find_element(self._input_locator).send_keys(keyword)
        return self

    def stock_join_or_delete(self):
        self.find_element_and_click(self._join_or_delete_locator)
        return self

    def toast_join_or_delete(self):
        return self.find_element(self._toast_or_delete_locator).text
