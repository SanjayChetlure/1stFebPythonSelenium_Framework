import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from PageClasses.Login1 import SwagLabLoginPage


class Test_SwagLagLogin:

    def test_TC1_loginToApp_titleValidation(self):
        username="standard_user"
        password="secret_sauce"
        app_url="https://www.saucedemo.com/"

        driver=webdriver.Chrome()
        driver.get(app_url)
        driver.implicitly_wait(5)

        login=SwagLabLoginPage(driver)
        login.enterUsername(username)
        login.enterPassword(password)
        login.clickOnLoginBtn()

        actTitle=driver.title
        expTilte="Swag Labs"

        if actTitle==expTilte:
            assert True
        else:
            assert False
        time.sleep(3)


    def test_TC2_loginWithInvalidCredentials(self):
        Invalidusername = "dkljgfff"
        Invalidpassword = "osfeoifhewd"
        app_url = "https://www.saucedemo.com/"

        driver = webdriver.Chrome()
        driver.get(app_url)
        driver.implicitly_wait(5)
        login=SwagLabLoginPage(driver)
        login.enterUsername(Invalidusername)
        login.enterPassword(Invalidpassword)
        login.clickOnLoginBtn()

        time.sleep(10)
