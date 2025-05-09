import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Login1 import SwagLabLoginPage
from UtilityFiles.customLogger import LogGen
from UtilityFiles.readProperties import ReadConfig


class Test_SwagLagLogin:
    username = ReadConfig.getAppUsername()      # username = "standard_user"
    password = ReadConfig.getAppPassword()      #  password = "secret_sauce"
    app_url = ReadConfig.getAppUrl()             # app_url = "https://www.saucedemo.com/"
    logger=LogGen.loggen()

    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
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
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(3)


    def test_TC2_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----Test Case execution started-------")
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
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
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(3)

