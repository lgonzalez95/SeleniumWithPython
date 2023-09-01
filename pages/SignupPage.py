import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class SignupPage:
    driver: WebDriver

    gender_male = (By.ID, "id_gender1")
    gender_female = (By.ID, "id_gender2")
    password = (By.ID, "password")
    dob_days = (By.ID, "days")
    dob_month = (By.ID, "months")
    dob_year = (By.ID, "years")
    subscribe_newsletter = (By.ID, "newsletter")
    subscribe_offers = (By.ID, "optin")

    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    company = (By.ID, "company")
    address_line_1 = (By.ID, "address1")
    address_line_2 = (By.ID, "address2")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zip_code = (By.ID, "zipcode")
    mobile_number = (By.ID, "mobile_number")
    create_account_btn = (By.CSS_SELECTOR, "button[data-qa='create-account']")

    def __init__(self, driver):
        self.driver = driver

    def enter_account_info(self, account_info, registration_data):
        if registration_data["Title"] == "Mr.":
            self.driver.find_element(*SignupPage.gender_male).click()
        else:
            self.driver.find_element(*SignupPage.gender_female).click()
        self.driver.find_element(*SignupPage.password).send_keys(account_info.password)
        days = Select(self.driver.find_element(*SignupPage.dob_days))
        month = Select(self.driver.find_element(*SignupPage.dob_month))
        year = Select(self.driver.find_element(*SignupPage.dob_year))
        days.select_by_index(account_info.dob.day)
        month.select_by_value(str(account_info.dob.month))
        year.select_by_value(str(account_info.dob.year))
        if registration_data["Subscribe newsletter"] == "Yes":
            self.driver.find_element(*SignupPage.subscribe_newsletter).click()
        if registration_data["Subscribe offers"] == "Yes":
            self.driver.find_element(*SignupPage.subscribe_offers).click()

    def enter_address_info(self, personal_info, address_info):
        self.driver.find_element(*SignupPage.first_name).send_keys(personal_info.first_name)
        self.driver.find_element(*SignupPage.last_name).send_keys(personal_info.last_name)
        self.driver.find_element(*SignupPage.company).send_keys(personal_info.company)
        self.driver.find_element(*SignupPage.address_line_1).send_keys(address_info.address_line_1)
        self.driver.find_element(*SignupPage.address_line_2).send_keys(address_info.address_line_2)
        country = Select(self.driver.find_element(*SignupPage.country))
        country.select_by_visible_text(address_info.country)
        self.driver.find_element(*SignupPage.state).send_keys(address_info.state)
        self.driver.find_element(*SignupPage.city).send_keys(address_info.city)
        self.driver.find_element(*SignupPage.zip_code).send_keys(address_info.zip_code)
        self.driver.find_element(*SignupPage.mobile_number).send_keys(personal_info.mobile_number)

    def create_account(self):
        self.driver.find_element(*SignupPage.create_account_btn).click()
