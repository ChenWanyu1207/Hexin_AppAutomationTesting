from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from time import sleep


class BasePage:
    _black_list = [
        (By.ID, "ok_btn"),
        (By.ID, "layout_first_level_no_exp"),
        (By.ID, "layout_second_level_hangqing"),
        (By.ID, "img_close")
    ]
    _black_other_bounds_list = [
        (By.ID, "show_content"),
        (By.ID, "bubble_guide_content")
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.x = self.driver.get_window_size()['width']
        self.y= self.driver.get_window_size()['height']

    def find_element(self, locator):
        print(locator)
        try:
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            self.handle_other_exception()
            # self.find_element(locator)
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        print("click")
        try:
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        print("exception running:")
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            elements = self.driver.find_elements(*locator)
            if len(elements) >= 1:
                elements[0].click()
            else:
                print("%s not found" % str(locator))

        self.driver.implicitly_wait(10)

    def handle_other_exception(self):
        print("exception other running:")
        page_source = self.driver.page_source
        # print(page_source)
        self.driver.implicitly_wait(10)
        for locator_others in self._black_other_bounds_list:
            if locator_others[1] in page_source:
                self.driver.tap([(918, 413), (1026, 521)], 100)
            else:
                print("%s not found or bounds error" % str(locator_others))
        self.driver.implicitly_wait(10)
