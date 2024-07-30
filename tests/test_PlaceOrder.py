import allure
import pytest
from allure_commons.types import AttachmentType

from Pages.cart_page import CartPage
from Pages.loginPage import LoginPage
from Pages.product_page import ProductPage
from Utils.readProperties import ReadConfig


class Test_001_Login:
    sauceDemoURL = ReadConfig().getbaseUrl()
    username = ReadConfig().getUsername()
    password = ReadConfig().getPasswo2rd()

    @pytest.mark.regression
    @pytest.mark.nkosi
    @allure.severity(allure.severity_level.CRITICAL)
    def test_loginTests(self, setup):
        self.driver = setup
        self.driver.get(self.sauceDemoURL)
        #self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.prod = ProductPage(self.driver)
        self.cart = CartPage(self.driver)

        self.lp.clickMainLoginButton()
        self.lp.enterUsername(self.username)
        self.lp.enterPassword(self.password)
        self.lp.clickLoginButton()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login page", attachment_type=AttachmentType.PNG)
        self.prod.select_device("Samsung galaxy s6")
        allure.attach(self.driver.get_screenshot_as_png(), name="Cart page", attachment_type=AttachmentType.PNG)
        self.cart.add_to_cart()
        allure.attach(self.driver.get_screenshot_as_png(), name="Shipping page", attachment_type=AttachmentType.PNG)
        self.cart.click_add_to_cart_btn()
        self.cart.verify_device_added()
        allure.attach(self.driver.get_screenshot_as_png(), name="Alert", attachment_type=AttachmentType.PNG)
        self.cart.accept_device_added_to_cart_alert()
        #self.driver.quit()
