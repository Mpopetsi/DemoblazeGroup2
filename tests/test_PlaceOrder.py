import time

import allure
import pytest
from allure_commons.types import AttachmentType
from faker import Faker

from Pages.loginPage import LoginPage
from Pages.productPage import ProductPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    baseURL = ReadConfig().getbaseUrl()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPasswo2rd()

    faker = Faker()
    Faker_Username = faker.first_name()

    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.productpage = ProductPage(self.driver)

        self.lp.clickMainLoginButton()
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        time.sleep(5)
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.lp.clickLoginButton()
        self.productpage.verifyLoginSuccess()
        # ToDo implemente the verifcation of home page
        allure.attach(self.driver.get_screenshot_as_png(), name="Product page", attachment_type=AttachmentType.PNG)
        self.productpage.selectSamsungGalaxyX6()
        allure.attach(self.driver.get_screenshot_as_png(), name="Add To Cart page", attachment_type=AttachmentType.PNG)
        self.productpage.clickAddToCart()
        self.productpage.acceptAlert()
        self.productpage.clickCart()
        allure.attach(self.driver.get_screenshot_as_png(), name="Cart", attachment_type=AttachmentType.PNG)
        time.sleep(5)

        self.driver.quit()
