from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class AccountCreated:
    driver: WebDriver

    account_created_msg = (By.CSS_SELECTOR, "*[data-qa='account-created']")
    continue_btn = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def __init__(self, driver):
        self.driver = driver

    def get_account_created_el(self):
        return self.driver.find_element(*AccountCreated.account_created_msg)

    def continue_to_home(self):
        self.driver.find_element(*AccountCreated.continue_btn).click()
