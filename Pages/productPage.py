import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage:

    SamsungGalaxyX6_xpath = "//a[@href='prod.html?idp_=1'][contains(.,'Samsung galaxy s6')]"

    def __init__(self, driver):
        self.driver = driver

    def selectSamsungGalaxyX6(self):
        time.sleep(5)
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.SamsungGalaxyX6_xpath)))
        element.click()




