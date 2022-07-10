import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
# passing the data to verify login functionality
@pytest.mark.parametrize("user, password",
                         [("anushapandit123@gmail.com", "j7qRhh-aB8ttkqi"), ("invalid_user@gmail.com", "00000000")])
class TestLogInRegisteredAccount():
    log = Utils.custom_logger()

# Create an instance of class
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LoginPage(self.driver)
        self.hp = HomePage(self.driver)
        self.ut = Utils()

# test case for login functionality with username and password
    def test_login_credentials(self, user, password):
        self.lp.do_click(self.lp.ACCEPT_PROMT)
        self.lp.do_send_keys(self.lp.USERNAME_TXT, user)
        self.lp.do_send_keys(self.lp.PASSWORD_TXT, password)
        if user == "anushapandit123@gmail.com" and password == "j7qRhh-aB8ttkqi":
            self.lp.do_click(self.lp.REGISTER_BUTTON)
            self.log.info("Login Successful")
        else:
            self.lp.do_click(self.lp.REGISTER_BUTTON)
            self.log.error("Login Failed")







