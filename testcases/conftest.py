import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import logging


# create setup method
@pytest.fixture(autouse=True)
def setup(request, browser, url):
    # For multiple browser selection
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        logging.critical("Provide valid browser")
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()


# Add command line option
def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")


# create fixture function for command line option browser
@pytest.fixture(scope="function", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# create fixture function for command line option url
@pytest.fixture(scope="function", autouse=True)
def url(request):
    return request.config.getoption("--url")


