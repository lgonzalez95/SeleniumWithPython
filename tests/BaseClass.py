import inspect

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class BaseClass:

    def get_logger(self):
        test_case_name = inspect.stack()[1][3]
        logger = logging.getLogger(test_case_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s => %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
