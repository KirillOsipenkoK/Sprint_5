from data import Person
from locators import (
    MainPageLocators,
    AuthPageLocators,
    RegistrationPageLocators,
    RecoverPageLocators
)
from urls import URLS
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_in_login_btn_success(self, driver):
        # Вход в личный кабинет через кнопку "Войти в аккаунт" на главной странице
        driver.get(URLS.MAIN_PAGE_URL)  # Открываем главную страницу
        driver.find_element(*MainPageLocators.login_account_btn).click()  # Жмём "Войти в аккаунт"
        driver.find_element(*AuthPageLocators.email_input).send_keys(Person.email)  # Вводим email
        driver.find_element(*AuthPageLocators.password_input).send_keys(Person.password)  # Вводим пароль
        driver.find_element(*AuthPageLocators.login_account_btn).click()  # Жмём кнопку входа
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.place_order_button)
        )  # Ждём появления кнопки "Оформить заказ"
        order_btn = driver.find_element(*MainPageLocators.place_order_button).text  # Получаем текст кнопки
        assert (driver.current_url == URLS.MAIN_PAGE_URL) and (order_btn == 'Оформить заказ')  # Проверяем URL и текст