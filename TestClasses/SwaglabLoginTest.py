import time
from selenium import webdriver
from PageClasses.Login1 import SwagLabLoginPage


class Test_SwagLagLogin:

    def test_TC1_loginToApp(self):
        driver=webdriver.Chrome()
        driver.get("https://www.saucedemo.com/")
        driver.implicitly_wait(5)

        login=SwagLabLoginPage(driver)
        login.enterUsername()
        login.enterPassword()
        login.clickOnLoginBtn()

        time.sleep(10)
