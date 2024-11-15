#pages/login_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "p.oxd-text.oxd-text--p.oxd-alert-content-text")

    def login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
