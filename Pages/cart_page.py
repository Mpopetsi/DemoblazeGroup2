import time

import faker
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class CartPage:
    __faker = Faker()
    __product_title = "//h2[@class='name'][contains(.,'Samsung galaxy s6')]"
    __add_to_cart_btn = "//a[contains(.,'Add to cart')]"
    __click_add_to_cart__btn = ''
    __alert_popup = ''
    __cart_button_xpath = "//a[@class='nav-link'][contains(.,'Cart')]"
    __time_out = 30
    __cart_items_table_id = 'tbodyid'
    __plac_order_button_xpath = "//button[contains(.,'Place Order')]"
    __shipping_name_id = 'name'
    __shipping_country_id = 'country'
    __shipping_city_id = 'city'
    __shipping_card_id = 'card'
    __shipping_month_id = 'month'
    __shipping_year_id = 'year'
    __purchase_button_xpath = "//button[contains(.,'Purchase')]"
    __purchase_info_xpath = "//p[@class='lead text-muted ']"

    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        try:
            WebDriverWait(self.driver, self.__time_out).until(
                EC.visibility_of_element_located((By.XPATH, self.__product_title))
            )
            self.__click_add_to_cart__btn = WebDriverWait(self.driver, self.__time_out).until(
                EC.element_to_be_clickable((By.XPATH, self.__add_to_cart_btn))
            )
        except Exception as e:
            print(f'An error occurred: {e}')

    def click_add_to_cart_btn(self):
        self.__click_add_to_cart__btn.click()

    def verify_device_added(self):
        self.__alert_popup = WebDriverWait(self.driver, self.__time_out).until(
            EC.alert_is_present()
        )

        if self.__alert_popup:
            self.__alert_popup = self.driver.switch_to.alert

    def accept_device_added_to_cart_alert(self):
        self.__alert_popup.accept()

    def go_to_cart_page(self):
        (WebDriverWait(self.driver, self.__time_out)
         .until(EC.element_to_be_clickable((By.XPATH, self.__cart_button_xpath)))
         .click())

    def get_cart_items_url(self):
        return self.driver.current_url

    def get_cart_items(self):
        table_data = (WebDriverWait(self.driver, self.__time_out)
                      .until(EC.visibility_of_element_located((By.ID, self.__cart_items_table_id))))

        time.sleep(5)

        items = table_data.find_elements(By.CLASS_NAME, "success")

        for item in items:
            if item.find_elements(By.TAG_NAME, 'td')[1].text.__eq__('Samsung galaxy s6'):
                device = item.find_elements(By.TAG_NAME, 'td')[1].text
                print(f'Device in cart: {device}')

    def click_place_order_btn(self):
        (WebDriverWait(self.driver, self.__time_out)
         .until(EC.element_to_be_clickable((By.XPATH, self.__plac_order_button_xpath)))
         .click())

    def populate_shipping_details(self):

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_name_id))))
         .send_keys(self.__faker.name()))

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_country_id))))
         .send_keys(self.__faker.country()))

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_city_id))))
         .send_keys(self.__faker.city()))

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_card_id))))
         .send_keys(self.__faker.credit_card_number()))

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_month_id))))
         .send_keys(self.__faker.month()))

        ((WebDriverWait(self.driver, self.__time_out)
          .until(EC.visibility_of_element_located((By.ID, self.__shipping_year_id))))
         .send_keys(self.__faker.year()))

    def click_purchase_btn(self):
        (WebDriverWait(self.driver, self.__time_out)
         .until(EC.visibility_of_element_located((By.XPATH, self.__purchase_button_xpath)))
         .click())

    def get_product_id(self):
        product_info = (WebDriverWait(self.driver, self.__time_out)
                        .until(EC.visibility_of_element_located((By.XPATH, self.__purchase_info_xpath))))

        split_data = product_info.text.split(' ')[1].split("\n")[0]
        print(f'Product ID: {split_data}')
