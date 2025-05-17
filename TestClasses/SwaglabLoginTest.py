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

    @pytest.mark.sanity
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

    @pytest.mark.sanity
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

    @pytest.mark.regression
    def test_TC3_verifyProductSize(self, openbrowser):
        self.logger.info("----test_TC3_verifyProductSize-------")
        driver = openbrowser
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        actProductSize = home.getAllProductSize()
        expProductSize = ReadTD.getTestDataInt(3, 1)

        if actProductSize == expProductSize:
            assert True
            self.logger.info("----Passed- Act & Exp product Size match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC3_verifyProductSize.png")
            self.logger.error("----Failed- Act & Exp product size mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    @pytest.mark.regression
    def test_TC4_verifyProductPrice(self, openbrowser):
        self.logger.info("----test_TC4_verifyProductPrice-------")
        driver = openbrowser
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        actProductPrice = float(home.getBackpackProductPrice())
        expProductPrice = float(ReadTD.getTestData(4, 1))

        if actProductPrice == expProductPrice:
            assert True
            self.logger.info("----Passed- Act & Exp product Price match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC4_verifyProductPrice.png")
            self.logger.error("----Failed- Act & Exp product price mist-match----")
            assert False
        time.sleep(3)
        driver.quit()

    @pytest.mark.smoke
    @pytest.mark.functional
    def test_TC5_verifyProductAllPrice(self, openbrowser):
        self.logger.info("----test_TC5_verifyProductAllPrice-------")
        driver = openbrowser
        self.loginToApp(driver)

        home = SwagLabHomePage(driver)
        actTotalPrice = home.getAllProductTotalPrice()
        expTotalPrice = float(ReadTD.getTestData(5, 1))

        if actTotalPrice == expTotalPrice:
            assert True
            self.logger.info("----Passed- Act & Exp Total Price match----")
        else:
            driver.save_screenshot(".\\SS\\test_TC5_verifyProductAllPrice.png")
            self.logger.error("----Failed- Act & Exp Total price mist-match----")
            assert False
        time.sleep(3)
        driver.quit()










