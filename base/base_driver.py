from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver():
    """create driver instance"""
    def __init__(self, driver):
        self.driver = driver

    # Wait until the element is present
    def wait_for_presence_of_element(self, locator):
        wait = WebDriverWait(self.driver, 10)
        element_name = wait.until(EC.presence_of_element_located(locator))
        return element_name

    # wait until the element is clickable
    def wait_until_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        click_element = wait.until(EC.element_to_be_clickable(locator))
        return click_element

    # wait until the element is visible
    def wait_until_visibility_of_element_located(self, locator):
        wait = WebDriverWait(self.driver, 10)
        click_element = wait.until(EC.visibility_of_element_located(locator))
        return click_element

