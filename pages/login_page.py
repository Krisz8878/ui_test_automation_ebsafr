import logging
from selenium.webdriver.common.by import By
from utils.config import Config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self):
        self.enter_username(Config.USERNAME)
        self.enter_password(Config.PASSWORD)
        self.click_login()

    def enter_username(self, username):
        logging.info(f"Entering username: {username}")
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        logging.info("Entering password.")
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        logging.info("Clicking login button.")
        self.driver.find_element(*self.login_button).click()