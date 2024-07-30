from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    __product_title = "//h2[@class='name'][contains(.,'Samsung galaxy s6')]"
    __add_to_cart_btn = "//a[contains(.,'Add to cart')]"
    __click_add_to_cart__btn = ''
    __alert_popup = ''

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, self.__product_title))
            )
            self.__click_add_to_cart__btn = WebDriverWait(self.driver, 30).until(
                EC.element_to_be_clickable((By.XPATH, self.__add_to_cart_btn))
            )
        except Exception as e:
            print(f'An error occurred: {e}')

    def click_add_to_cart_btn(self):
        self.__click_add_to_cart__btn.click()

    def verify_device_added(self):
        self.__alert_popup = WebDriverWait(self.driver, 30).until(
            EC.alert_is_present()
        )

        if self.__alert_popup:
            print('Device added!')
            self.__alert_popup = self.driver.switch_to.alert

    def accept_device_added_to_cart_alert(self):
        self.__alert_popup.accept()
