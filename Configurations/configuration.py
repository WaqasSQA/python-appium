import time
import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService


@pytest.fixture(scope='module')
def setup_appium_driver():
    appium_service = AppiumService()
    appium_service.start()

    desired_caps = {
        'platformName': 'Android',
        'deviceName': 'Redmi 12C',
        'app': '',
        'automationName': 'UiAutomator2',
        'fullReset': True,
        'autoGrantPermissions': True,
        # Set to True to avoid resetting app data
        # Add other desired capabilities as needed
    }

    # Initialize Driver
    driver = webdriver.Remote('https//:127.0.0.1:4723', desired_caps)
    time.sleep(10)

    # Any Setup Action to be performed

    # // Here.....

    # Yield Driver

    yield driver
    driver.quit()
    appium_service.start()
