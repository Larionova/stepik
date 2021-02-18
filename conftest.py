import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--driver', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope='function')
def driver(request):
    driver_name = request.config.getoption('driver')
    driver = None
    if driver_name == 'chrome':
        driver = webdriver.Chrome()
    elif driver_name == 'firefox':
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError('--driver should be chrome or firefox')
    yield driver
    driver.quit()

