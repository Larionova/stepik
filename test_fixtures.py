import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.mark.parametrize('url', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1",
                                 "236903/step/1", "236904/step/1", "236905/step/1"])
class TestLogin:
    def test_guest_should_see_login_link(self, driver, url):
        link = f"https://stepik.org/lesson/{url}"
        driver.get(link)
        text_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea')))
        text_area.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        button.click()
        smart_hint = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))
        smart_text = smart_hint.text
        assert smart_text == "Correct!", f"Wrong {smart_text}"
