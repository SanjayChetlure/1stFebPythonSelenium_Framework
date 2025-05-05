import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

from PageClasses.Login1 import SwagLabLoginPage


class Test_SwagLagLogin:

    def test_TC1_loginToApp_titleValidation(self,openbrowser):
        username="standard_user"
        password="secret_sauce"
        app_url="https://www.saucedemo.com/"

        driver=openbrowser
        driver.get(app_url)
        driver.implicitly_wait(5)

        login=SwagLabLoginPage(driver)
        login.enterUsername(username)
        login.enterPassword(password)
        login.clickOnLoginBtn()

        actTitle=driver.title
        expTilte="Swag Labs1"

        if actTitle==expTilte:
            assert True
        else:
            driver.save_screenshot(".\\SS\\test_TC1_loginToApp_titleValidation.png")
            assert False
        time.sleep(3)


    # def test_TC2_loginWithInvalidCredentials(self,openbrowser):
    #     Invalidusername = "dkljgfff"
    #     Invalidpassword = "osfeoifhewd"
    #     app_url = "https://www.saucedemo.com/"
    #
    #     driver = openbrowser
    #     driver.get(app_url)
    #     driver.implicitly_wait(5)
    #     login=SwagLabLoginPage(driver)
    #     login.enterUsername(Invalidusername)
    #     login.enterPassword(Invalidpassword)
    #     login.clickOnLoginBtn()
    #
    #     time.sleep(10)
