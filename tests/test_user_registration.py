import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestUserRegistration:
    @allure.title('Проверка успешной регистрации нового пользователя')
    @allure.description('Проверяем успешную авторизацию нового пользователя с указанием всех полей')
    def test_reg_new_user(self, random_user_data_for_registration):
        response_registration = StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)

        assert response_registration.status_code == 200 and response_registration.json()['success'] is True

    @allure.title('Проверка повторной регистрации пользователя')
    @allure.description('Проверка регистрации пользователя, который уже зарегистрирован в системе')
    def test_reg_existing_user(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_registration = StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)

        assert response_registration.status_code == 403 and response_registration.json()['success'] is False

    @allure.title('Проверка регистрации пользователя без пароля')
    @allure.description('Проверка регистрации пользователя без указания пароля ')
    def test_reg_user_without_password(self, random_user_data_for_registration):
        random_user_data_for_registration_copy = random_user_data_for_registration.copy()
        del random_user_data_for_registration_copy["password"]
        response_registration = StellarBurgerApi.stellar_registration_user(random_user_data_for_registration_copy)

        assert response_registration.status_code == 403 \
               and response_registration.json()['message'] == 'Email, password and name are required fields'
