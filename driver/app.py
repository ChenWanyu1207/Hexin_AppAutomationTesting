import datetime
import os
from time import sleep
from appium import webdriver
from selenium.webdriver.common import utils
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from page.main_page import MainPage


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "honnor_10"
        caps["appPackage"] = "com.hexin.plat.android"
        # caps["uiautomationName"] = "uiautomator2"
        caps["appActivity"] = ".AndroidLogoActivity"
        caps["autoGrantPermissions"] = "true"
        # caps["udid"] = "emulator-5554"
        caps["udid"] = "VBJ0218818001230"
        # udid = os.getenv("udid",None)
        # if udid !=None:
        #     caps["udid"]=udid
        # caps["systemPort"]=utils.free_port() #手机uiautomator server 占用6790端口，forward到8100的pc端口，8100容易起冲突
        # caps["showchromedriverPort"] = utils.free_port()
        caps['chromedriverExecutable'] = '/Users/ljw/cwy/cwy_documents/chromedriver/2.20/chromedriver'
        caps["showChromedriverLog"] = True
        caps["unicodeKeyBoard"] = True
        caps["autoGrantPermissions"] =True
        caps["skipServerInstallation"] =False
        caps["skipDeviceInitialization"]=False

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        # cls.driver = webdriver.Remote("http://localhost:4444/wd/hub", caps)
        cls.driver.implicitly_wait(10)
        # sleep(3)
        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()
