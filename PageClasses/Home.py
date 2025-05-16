from selenium.webdriver.common.by import By
from selenium import webdriver

class SwagLabHomePage:

    #1: declare web elements globally
    textBackpackProductXpath="//div[text()='Sauce Labs Backpack']"
    allProdictSizeXpath="//div[@class='inventory_item_name ']"
    textBackpackProductPriceXpath = "(//div[@class='inventory_item_price'])[1]"


    #2: initialization webdriver object globally
    def __init__(self,driver):
        self.driver=driver

    #3: perform actions
    def getBackpackProductName(self):
        productName=self.driver.find_element(By.XPATH,self.textBackpackProductXpath).text
        return productName

    def getAllProductSize(self):
        allProduct=self.driver.find_elements(By.XPATH,self.allProdictSizeXpath)
        size=len(allProduct)
        return size

    def getBackpackProductPrice(self):
        productPrice=self.driver.find_element(By.XPATH,self.textBackpackProductPriceXpath).text
        productPrice=productPrice[1:]
        return productPrice



