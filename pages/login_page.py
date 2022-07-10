import logging
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.utils import Utils


class LoginPage(BaseDriver):
    log = Utils.custom_logger(log_level=logging.WARNING)

    # List of Locators
    ACCEPT_PROMT = (By.ID, "popin_tc_privacy_button")
    USERNAME_TXT = (By.ID, "login_email")
    PASSWORD_TXT = (By.ID, "login_password")
    REGISTER_BUTTON = (By.XPATH, "//button[@class='button button--primary button--large _fit _mt3 lg_c-auto lg_mt0']")
    INVALID_NOTIFICATION = (By.XPATH, "//font[normalize-space()='Your account was not recognised.']")
    LOGIN_NOTIFICATION = (By.XPATH, "//font[contains(text(),'You are now registered with Contorion.')]")

    """create driver instance"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # For click event
    def do_click(self, locator):
        self.wait_until_element_is_clickable(locator).click()

    # To send credentials
    def do_send_keys(self, locator, text):
        self.wait_until_visibility_of_element_located(locator).send_keys(text)

    # To get the text of the notification
    def notification_message(self, locator):
        notification_msg = self.wait_until_visibility_of_element_located(locator).text
        self.log.info(notification_msg)













