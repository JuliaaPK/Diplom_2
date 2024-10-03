import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestChangeUserInfo:
    @allure.title('Проверка изменения пароля авторизованного пользователя')
    @allure.description('Проверка изменения поля password для авторизованного пользователя')
    def test_change_authorized_user_password(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        random_user_data_for_registration["password"] = Helpers.generate_new_password()

        response_update = StellarBurgerApi \
            .stellar_update_user_info(random_user_data_for_registration, response_access_token)

        assert response_update.status_code == 200 and response_update.json()["success"] is True

    @allure.title('Проверка изменения email авторизованного пользователя')
    @allure.description('Проверка изменения поля email для авторизованного пользователя')
    def test_change_authorized_user_email(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        random_user_data_for_registration["email"] = Helpers.generate_new_email()

        response_update = StellarBurgerApi \
            .stellar_update_user_info(random_user_data_for_registration, response_access_token)

        assert response_update.status_code == 200 and response_update.json()["success"] is True

    @allure.title('Проверка изменения name авторизованного пользователя')
    @allure.description('Проверка изменения поля name для авторизованного пользователя')
    def test_change_authorized_user_name(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        random_user_data_for_registration["name"] = Helpers.generate_new_name()

        response_update = StellarBurgerApi \
            .stellar_update_user_info(random_user_data_for_registration, response_access_token)

        assert response_update.status_code == 200 and response_update.json()["success"] is True

    @allure.title('Проверка изменения email не авторизованного пользователя')
    @allure.description('Проверка изменения поля email для не авторизованного пользователя')
    def test_change_unauthorized_user_email(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        random_user_data_for_registration_copy = random_user_data_for_registration.copy()
        random_user_data_for_registration_copy["email"] = Helpers.generate_new_email()
        response_update = StellarBurgerApi.stellar_update_user_info(random_user_data_for_registration_copy)

        assert response_update.status_code == 401 and response_update.json()["message"] == "You should be authorised"

    @allure.title('Проверка изменения password не авторизованного пользователя')
    @allure.description('Проверка изменения поля password для не авторизованного пользователя')
    def test_change_unauthorized_user_password(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        random_user_data_for_registration_copy = random_user_data_for_registration.copy()
        random_user_data_for_registration_copy["password"] = Helpers.generate_new_password()
        response_update = StellarBurgerApi.stellar_update_user_info(random_user_data_for_registration_copy)

        assert response_update.status_code == 401 and response_update.json()["message"] == "You should be authorised"

    @allure.title('Проверка изменения name не авторизованного пользователя')
    @allure.description('Проверка изменения поля name для не авторизованного пользователя')
    def test_change_unauthorized_user_name(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        random_user_data_for_registration_copy = random_user_data_for_registration.copy()
        random_user_data_for_registration_copy["name"] = Helpers.generate_new_name()
        response_update = StellarBurgerApi.stellar_update_user_info(random_user_data_for_registration_copy)

        assert response_update.status_code == 401 and response_update.json()["message"] == "You should be authorised"