import random
import string

import allure

from stellar_burger_api import StellarBurgerApi


class Helpers:
    @staticmethod
    @allure.step("Создание случайного email для пользователя")
    def generate_new_email():
        return f'testUserReg{random.randint(100, 999)}@yandex.ru'

    @staticmethod
    @allure.step("Создание случайного password для пользователя")
    def generate_new_password():
        return f'{random.randint(100000, 999999)}'

    @staticmethod
    @allure.step("Создание случайного name для пользователя")
    def generate_new_name():
        return f'user{random.randint(100, 999)}'

    @staticmethod
    @allure.step("Создание случайного пользователя")
    def create_random_user_data_for_registration():
        return {
            "email": Helpers.generate_new_email(),
            "password": Helpers.generate_new_password(),
            "name": Helpers.generate_new_name()
        }

    @staticmethod
    @allure.step("Создание списка fake hash ingredients")
    def create_list_with_fake_hash_ingredients(number):
        return list(map(lambda x: Helpers.generate_random_string(24), range(number)))

    @staticmethod
    @allure.step("Генерация случайной строки фиксированной длины")
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step("Получние токена пользователя")
    def get_user_access_token(user_data):
        response_auth = StellarBurgerApi.stellar_auth_user(user_data)

        if response_auth.status_code == 200:
            return response_auth.json()["accessToken"]

    @staticmethod
    @allure.step("Удаление пользователя по его данным")
    def delete_user_if_exists(user_data):
        user_access_token = Helpers.get_user_access_token(user_data)

        if user_access_token is not None:
            StellarBurgerApi.stellar_delete_user(user_access_token)

    @staticmethod
    @allure.step("Получение всех доступных ингредиентов")
    def get_all_available_ingredient():
        return StellarBurgerApi.get_all_available_ingredients().json()["data"]

    @staticmethod
    @allure.step("Получение hash n-ингредиентов")
    def get_hash_list_of_n_first_ingredients(n):
        return list(map(lambda ingredient: ingredient["_id"], Helpers.get_all_available_ingredient()[0:n]))
