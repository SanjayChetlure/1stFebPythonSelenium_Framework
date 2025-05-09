from email.policy import default

import pytest
from  selenium import  webdriver

#step3: modify fixture for multiple browser
@pytest.fixture
def openbrowser(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        return driver
    elif browser=="edge":
        driver=webdriver.Edge()
        return driver
    elif browser=="firefox":
        driver=webdriver.Firefox()
        return driver

#Step2: use to get browser name from command - line & pass value browser to openbrowser fixture
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

#step1: set default value of browser
def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",
                     help="provide browser name - chrome, firefox, edge, etc")