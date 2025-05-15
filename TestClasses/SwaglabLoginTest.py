import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Home import SwagLabHomePage
from PageClasses.Login1 import SwagLabLoginPage
from UtilityFiles.ReadExcel import ReadTD
from UtilityFiles.customLogger import LogGen
from UtilityFiles.readProperties import ReadConfig


class Test_SwagLagLogin:

    logger=LogGen.loggen()

    def loginToApp(self,driver):
        login = SwagLabLoginPage(driver)
        login.enterUsername(ReadConfig.getAppUsername())
        login.enterPassword(ReadConfig.getAppPassword())
        login.clickOnLoginBtn()

    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        self.logger.info("----test_TC1_loginToApp_titleValidation-------")
        driver=openbrowser
        self.loginToApp(driver)

        actTitle=driver.title
        expTilte=ReadTD.getTestData(1,1)

        if actTitle==expTilte:
            assert True
            self.logger.info("----Passed- Act & Exp Title match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            self.logger.error("----Failed- Act & Exp Title mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    def test_TC2_verifyProductName(self, openbrowser):
        self.logger.info("----test_TC2_verifyProductName-------")
        driver = openbrowser
        self.loginToApp(driver)

        home=SwagLabHomePage(driver)
        actProductName=home.getBackpackProductName()
        expProductName=ReadTD.getTestData(2,1)

        if actProductName == expProductName:
            assert True
            self.logger.info("----Passed- Act & Exp product name match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC2_verifyProductName.png")
            self.logger.error("----Failed- Act & Exp product name mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    def test_TC3_verifyProductSize(self, openbrowser):

        time.sleep(3)






