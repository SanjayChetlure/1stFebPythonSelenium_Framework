import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Login1 import SwagLabLoginPage
from UtilityFiles.readProperties import ReadConfig


class Test_SwagLagLogin:
    username = ReadConfig.getAppUsername()      # username = "standard_user"
    password = ReadConfig.getAppPassword()      #  password = "secret_sauce"
    app_url = ReadConfig.getAppUrl()             # app_url = "https://www.saucedemo.com/"

    def test_TC1_loginToApp_titleValidation(self,openbrowser):

        driver=openbrowser
        driver.get(self.app_url)
        driver.implicitly_wait(5)

        login=SwagLabLoginPage(driver)
        login.enterUsername(self.username)
        login.enterPassword(self.password)
        login.clickOnLoginBtn()

        actTitle=driver.title
        expTilte="Swag Labs"

        if actTitle==expTilte:
            assert True
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            assert False
        time.sleep(3)

