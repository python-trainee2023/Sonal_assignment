from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class BaseTest:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.sastotickets.com/")
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

class Test_login(BaseTest):
    # def test_loginss(self):
    #     first = self.driver.find_element(By.ID, "depart_city").click()
    #     self.send_keys("ktm")
    #     time.sleep(2)

    def test_log(self):
        self.driver.find_element(By.XPATH, "//*[@data-target='#login-modal']").click()
        self.driver.find_element(By.ID, "login_username").send_keys("sonal")
        self.driver.find_element(By.ID, "login_password").send_keys("helloo")
        time.sleep(2)




        # username = self.driver.find_element(By.ID, "user-name")
        # username.send_keys("standard_user")
        #
        #
        # password = self.driver.find_element(By.ID, "password")
        # password.send_keys("secret_sauce")
