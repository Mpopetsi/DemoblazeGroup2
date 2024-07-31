from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
Selenium Scenario – Practical Test:

Note: You have 45 minutes to complete this scenario.
 
In the test we require you to demonstrate the following automation practices:
Usage of Feature Files
Java Classes
Automation Best practices
Test Execution & Reporting
 
Automation Tool Recommendation:
Selenium
Rest Assured
Cucumber
 
Navigate to this website:
https://www.demoblaze.com/index.html
 
Login with
Username: admin
Password: admin
Select a Samsung galaxy s6
Add to the cart
Place order (enter random data in the fields)
Return the purchase ID
 
** If there are any items in the cart when you initially log in, please manually remove it, and continue with the question.
"""


class ProductPage:
    __product_link = "//a[contains(.,'Samsung galaxy s6')]"
    __time_out = 30
    __logged_in_user_xpath = "//a[contains(.,'Welcome admin')]"

    def __init__(self, driver):
        self.driver = driver

    def select_device(self, device):
        try:
            logged_in_user = WebDriverWait(self.driver, self.__time_out).until(
                EC.visibility_of_element_located((By.XPATH, self.__logged_in_user_xpath))).text

            if logged_in_user.__eq__('Welcome admin'):
                link = WebDriverWait(self.driver, self.__time_out).until(
                    EC.visibility_of_element_located((By.XPATH, self.__product_link)))
                self.driver.get(link.get_attribute('href'))
        except Exception as e:
            print(f'An error occurred: {e}')
