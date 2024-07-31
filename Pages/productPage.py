import time

from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:
    SamsungGalaxyX6_xpath = "//a[@href='prod.html?idp_=1'][contains(.,'Samsung galaxy s6')]"
    addToCart_xpath = "//a[@href='#'][contains(.,'Add to cart')]"
    Cart_xpath = "//a[@class='nav-link'][contains(.,'Cart')]"
    Logout_xpath = "//a[@class='nav-link'][contains(.,'Log out')]"

    def __init__(self, driver):
        self.driver = driver

    def verifyLoginSuccess(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Logout_xpath)))
        element.is_displayed()

    # def selectSamsungGalaxyX6(self):
    #     time.sleep(5)
    #     wait = WebDriverWait(self.driver, 15)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.SamsungGalaxyX6_xpath)))
    #     element.click()
    #
    #
    #
    # def clickAddToCart(self):
    #     time.sleep(5)
    #     wait = WebDriverWait(self.driver, 15)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.addToCart_xpath)))
    #     element.click()
    #
    # def acceptAlert(self):
    #     try:
    #         WebDriverWait(self.driver, 10).until(EC.alert_is_present())
    #         alert = self.driver.switch_to.alert
    #         alert.accept()
    #     except NoAlertPresentException:
    #         print("No alert is present")
    #
    # def clickCart(self):
    #     time.sleep(5)
    #     wait = WebDriverWait(self.driver, 15)
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, self.Cart_xpath)))
    #     element.click()
    #     time.sleep(5)
