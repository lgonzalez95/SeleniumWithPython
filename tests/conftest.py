import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.AccountCreated import AccountCreated
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.SignupPage import SignupPage
from utilities.ExcelDataReader import get_test_data_as_dict

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope='class')
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://automationexercise.com/")
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture
def signup_and_login_page_objects(request):
    home_page = HomePage(driver)
    login_page = LoginPage(driver)
    signup_page = SignupPage(driver)
    account_created_page = AccountCreated(driver)

    return home_page, login_page, signup_page, account_created_page


@pytest.fixture(params=get_test_data_as_dict(
    "/Users/luis.gonzalez.flores/Documents/SeleniumPythonFramework/test_data/signup_data.xlsx"))
def get_registration_test_data(request):
    return request.param


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
