from selenium.webdriver.common.by import By

class MainPageLocators:
    """Главная страница"""
    main_form = (By.CSS_SELECTOR, 'main.App_componentContainer__2JC2W')  # Форма главной страницы сайта
    logo_btn = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Кнопка главной страницы сайта
    personal_account_btn = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка личного кабинета
    login_account_btn = (By.LINK_TEXT, 'Войти в аккаунт')  # Кнопка войти в аккаунт
    constructor_btn = (By.LINK_TEXT, 'Конструктор')  # Кнопка конструктор
    order_feed_btn = (By.LINK_TEXT, 'Лента Заказов')  # Кнопка лента заказов
    bun_btn = (By.LINK_TEXT, 'Булки')  # Кнопка переключения на булки
    sauces_btn = (By.LINK_TEXT, 'Соусы')  # Кнопка переключения на соусы
    toppings_btn = (By.LINK_TEXT, 'Начинки')  # Кнопка переключения на начинки
    place_order_button = (By.LINK_TEXT, 'Оформить заказ')  # Кнопка оформить заказ
    sauces = (By.CSS_SELECTOR, 'h2:contains("Соусы")')  # Текст соусы на главной странице
    sauces_ul = (By.CSS_SELECTOR, 'ul.BurgerIngredients_ingredients__list__2A-mT')  # Выбор соусов на главной странице
    bun = (By.CSS_SELECTOR, 'h2:contains("Булки")')  # Текст булки на главной странице
    bun_ul = (By.CSS_SELECTOR, 'ul.BurgerIngredients_ingredients__list__2A-mT')  # Выбор булок на главной странице
    topping = (By.CSS_SELECTOR, 'h2:contains("Начинки")')  # Текст начинки на главной странице
    topping_ul = (By.CSS_SELECTOR, 'ul.BurgerIngredients_ingredients__list__2A-mT')  # Выбор начинок на главной странице

class AuthPageLocators:
    """Форма авторизации"""
    auth_form = (By.CSS_SELECTOR, 'div.Auth_login__3hAey')  # Форма авторизации
    email_input = (By.NAME, 'name')  # Поле ввода email
    password_input = (By.NAME, 'Пароль')  # Поле ввода пароля
    login_account_btn = (By.LINK_TEXT, 'Войти')  # Кнопка войти
    registration_btn = (By.LINK_TEXT, 'Зарегистрироваться')  # Кнопка зарегистрироваться
    recover_btn = (By.LINK_TEXT, 'Восстановить пароль')  # Кнопка восстановить пароль
    constructor_btn = (By.LINK_TEXT, 'Конструктор')  # Кнопка конструктор
    order_feed_btn = (By.LINK_TEXT, 'Лента Заказов')  # Кнопка лента заказов
    logo_btn = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Кнопка главной страницы сайта
    personal_account_btn = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка личного кабинета

class RegistrationPageLocators:
    """Форма регистрации"""
    name_input = (By.NAME, 'name')  # Поле ввода имени
    email_input = (By.NAME, 'email')  # Поле ввода email
    password_input = (By.NAME, 'Пароль')  # Поле ввода пароля
    registration_btn = (By.LINK_TEXT, 'Зарегистрироваться')  # Кнопка зарегистрироваться
    login_account_btn = (By.LINK_TEXT, 'Войти')  # Кнопка войти
    constructor_btn = (By.LINK_TEXT, 'Конструктор')  # Кнопка конструктор
    order_feed_btn = (By.LINK_TEXT, 'Лента Заказов')  # Кнопка лента заказов
    logo_btn = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Кнопка главной страницы сайта
    personal_account_btn = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка личного кабинета
    error_message_double_reg = (By.CSS_SELECTOR, 'p:contains("Такой пользователь уже существует")')  # Ошибка при повторной регистрации
    error_message_incorrect_password = (By.CSS_SELECTOR, 'p:contains("Некорректный пароль")')  # Ошибка при вводе некорректного пароля
class RecoverPageLocators:
    """Форма восстановления пароля"""
    email_input = (By.CSS_SELECTOR, 'label:contains("Email") + input')  # Поле ввода email
    recover_btn = (By.LINK_TEXT, 'Восстановить')  # Кнопка восстановить
    login_account_btn = (By.LINK_TEXT, 'Войти')  # Кнопка войти
    constructor_btn = (By.LINK_TEXT, 'Конструктор')  # Кнопка конструктор
    order_feed_btn = (By.LINK_TEXT, 'Лента Заказов')  # Кнопка лента заказов
    logo_btn = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Кнопка главной страницы сайта
    personal_account_btn = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка личного кабинета

class PersonalAreaLocators:
    """Форма личного кабинета"""
    profile_form = (By.CSS_SELECTOR, 'div.Account_account__vgk_w')  # Форма личного кабинета
    profile_btn = (By.LINK_TEXT, 'Профиль')  # Кнопка профиль
    order_history_btn = (By.LINK_TEXT, 'История заказов')  # Кнопка история заказов
    exit_btn = (By.LINK_TEXT, 'Выход')  # Кнопка выход
    save_btn = (By.LINK_TEXT, 'Сохранить')  # Кнопка сохранить
    cansel_btn = (By.LINK_TEXT, 'Отмена')  # Кнопка отмена
    constructor_btn = (By.LINK_TEXT, 'Конструктор')  # Кнопка конструктор
    order_feed_btn = (By.LINK_TEXT, 'Лента Заказов')  # Кнопка лента заказов
    logo_btn = (By.CSS_SELECTOR, 'div.AppHeader_header__logo__2D0X2')  # Кнопка главной страницы сайта
    personal_account_btn = (By.LINK_TEXT, 'Личный Кабинет')  # Кнопка личного кабинета
