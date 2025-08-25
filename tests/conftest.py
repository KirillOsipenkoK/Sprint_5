import os
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

load_dotenv()  # Загружаем переменные из .env

class TestBase:
    def setup_method(self):
        chrome_driver_path = os.getenv('CHROMEDRIVER_PATH')
        service = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)

import pytest
from locators import MainPageLocators, AuthPageLocators
from urls import URLS
from data import Person
from expected_texts import BUN_TEXT, SAUCES_TEXT, TOPPINGS_TEXT


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def get_login_driver(driver):
    driver.get(URLS.MAIN_PAGE_URL)
    driver.find_element(*MainPageLocators.personal_account_btn).click()
    driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)
    driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)
    driver.find_element(*AuthPageLocators.login_account_btn).click()

    return driver