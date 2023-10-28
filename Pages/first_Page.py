from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from BasePage.Base_Page import BasePage


class firstPage(BasePage):
    def first_locator(self):
        element_one = self.wait_for_element(By.XPATH, 'xpath')
        element_one.click()

    def wait_for_element(self, locator, locator_strategy):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((locator_strategy, locator)))
        return element
