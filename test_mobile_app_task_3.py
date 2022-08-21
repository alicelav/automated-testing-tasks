import pytest
import unittest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy


class AppiumTest(unittest.TestCase):
    driver = None
    platform_version = "10"
    app_package = "com.planet.forme"
    app_activity = "com.planet.forme.ui.activities.main.MainActivity"
    device_udid = "34HDU19B29002910"
    command_executor = "http://localhost:4723/wd/hub"

    def setUp(self):
        options = UiAutomator2Options()
        options.platformVersion = self.platform_version
        options.app_package = self.app_package
        options.app_activity = self.app_activity
        options.udid = self.device_udid

        self.driver = webdriver.Remote(self.command_executor, options=options)

    def testFirstAutomation(self):
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Вход']").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Логин']").send_keys("test555")
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Пароль']").send_keys("zujlrb6571")
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='ВОЙТИ']").click()
        self.driver.find_element(by=AppiumBy.ID, value="navigationGlobalSearch").click()
        self.driver.find_element(by=AppiumBy.XPATH, value="//*[@text='Поиск']").clear().send_keys("Москва" + "\n")
        assert self.driver.find_element(by=AppiumBy.ID, value="root")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
