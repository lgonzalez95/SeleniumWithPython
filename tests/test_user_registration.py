import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from tests.BaseClass import BaseClass
from utilities import DataFaker


class TestUserRegistration(BaseClass):
    driver: WebDriver

    @pytest.mark.usefixtures("signup_and_login_page_objects", "get_registration_test_data")
    def test_register_valid_user(self, signup_and_login_page_objects, get_registration_test_data):
        print(get_registration_test_data)
        logger = self.get_logger()
        home_page, login_page, signup_page, account_created_page = signup_and_login_page_objects
        personal_info = DataFaker.get_random_personal_info()
        account_info = DataFaker.get_random_account_info(personal_info)

        logger.info("Going to loging page")
        home_page.go_to_login_page()
        logger.info("Starting sing up")
        login_page.start_signup(account_info)
        logger.info("Entering account info: " + str(account_info))
        signup_page.enter_account_info(account_info, get_registration_test_data)
        address_info = DataFaker.get_random_address_info()
        logger.info("Entering personal and address info:\n" + str(personal_info) + "\n" + str(address_info))
        signup_page.enter_address_info(personal_info, address_info)
        logger.warning("Creating new account")
        signup_page.create_account()
        assert "ACCOUNT CREATED!" == account_created_page.get_account_created_el().text
        account_created_page.continue_to_home()
        home_page.delete_created_account()
