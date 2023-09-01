from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HomePage:
    signup_login = (By.CSS_SELECTOR, "a[href='/login']")
    delete_account = (By.PARTIAL_LINK_TEXT, "Delete Account")
    driver: WebDriver

    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.find_element(*HomePage.signup_login).click()

    def delete_created_account(self):
        self.driver.find_element(*HomePage.delete_account).click()
