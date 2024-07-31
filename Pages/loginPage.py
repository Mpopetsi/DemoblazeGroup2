from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    button_MainLogin_id = 'login2'
    textbox_username_id = 'loginusername'
    textbox_password_id = 'loginpassword'
    button_loginButton_xpath = "//button[contains(.,'Log in')]"


    def __init__(self, driver):
        self.driver = driver

    def clickMainLoginButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.button_MainLogin_id)))
        element.click()

    def enterUsername(self, username):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_username_id)))
        element.send_keys(username)

    def enterPassword(self, password):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.ID, self.textbox_password_id)))
        element.send_keys(password)

    def clickLoginButton(self):
        wait = WebDriverWait(self.driver, 15)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_loginButton_xpath)))
        element.click()


