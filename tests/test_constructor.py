from locators import MainPageLocators
from urls import URLS
from expected_texts import BUN_TEXT, SAUCES_TEXT, TOPPINGS_TEXT


class TestConstructorPage:

    def test_transition_to_bun_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.bun_btn).click()  # Нажимаем сразу на нужную вкладку

        # Добавляем проверку активного состояния вкладки
        active_bun_tab = driver.find_element(*MainPageLocators.bun_btn)
        assert 'active' in active_bun_tab.get_attribute('class')

        bun_text = driver.find_element(*MainPageLocators.bun).text
        assert bun_text == BUN_TEXT

    def test_transition_to_sauces_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()

        # Проверяем активный статус вкладки
        active_sauces_tab = driver.find_element(*MainPageLocators.sauces_btn)
        assert 'active' in active_sauces_tab.get_attribute('class')

        sauces = driver.find_element(*MainPageLocators.sauces).text
        assert sauces == SAUCES_TEXT

    def test_transition_to_topping_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()

        # Проверяем активный статус вкладки
        active_toppings_tab = driver.find_element(*MainPageLocators.toppings_btn)
        assert 'active' in active_toppings_tab.get_attribute('class')

        topping = driver.find_element(*MainPageLocators.topping).text
        assert topping == TOPPINGS_TEXT
