from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    driver: WebDriver

    signup_form = (By.CSS_SELECTOR, "form[action='/signup']")
    signup_name = (By.NAME, "name")
    signup_email = (By.NAME, "email")
    signup_btn = (By.TAG_NAME, "button")

    def __init__(self, driver):
        self.driver = driver

    def start_signup(self, account_info):
        self.driver.find_element(*LoginPage.signup_form).find_element(*LoginPage.signup_name).send_keys(
            account_info.name)
        self.driver.find_element(*LoginPage.signup_form).find_element(*LoginPage.signup_email).send_keys(
            account_info.email)
        self.driver.find_element(*LoginPage.signup_form).find_element(*LoginPage.signup_btn).click()
