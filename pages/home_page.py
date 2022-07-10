from base.base_driver import BaseDriver
from utilities.utils import Utils


class HomePage(BaseDriver):
    log = Utils.custom_logger()

    """create driver instance"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # sign out function
    def sign_out(self):
        pass

