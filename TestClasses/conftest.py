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


###-----Html Report----####
#1: It is hook for adding environment info into Report (customize info in report)
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Swag Labs'
    metadata['Module Name'] = 'Login'
    metadata['Tester Name'] = 'Sanjay'

    # # ✅ Remove unwanted keys if they exist
    # metadata.pop("JAVA_HOME", None)
    # metadata.pop("Plugins", None)

# def pytest_configure(config):
#     config._metadata['Project Name']='Swag labs'
#     config._metadata['Module Name'] = 'Login'
#     config._metadata['Tester Name'] = 'Sanjay'
#
#
# #2: It is Hook for delete/modify Environment info into Html Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME",None)
#     metadata.pop("Plugins", None)