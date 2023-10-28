import time
from Pages.first_Page import firstPage
from Configurations.configuration import setup_appium_driver
from Test_Data.test_Data import Username, Password


def test_login(setup_appium_driver):
    print("Test Started")
    driver = setup_appium_driver

    first_Page = firstPage(driver)

    first_Page.first_locator()


