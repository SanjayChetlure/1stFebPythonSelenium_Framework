import pytest
from  selenium import  webdriver

@pytest.fixture
def openbrowser():
    driver=webdriver.Chrome()
    return driver