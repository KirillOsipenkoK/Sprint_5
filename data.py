from random import randint

class Person:
    user_name = 'Miwkaaa'
    email = 'miwkaaaaaaaaaa@yandex.ru'
    password = 'Qwe123456'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'