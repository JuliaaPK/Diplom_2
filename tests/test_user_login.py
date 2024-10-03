import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestUserAuth:
    @allure.title('Проверка успешной авторизации пользователя')
    @allure.description('Проверка успешной авторизации ранее зарегистрированного пользователя')
    def test_auth_existing_user(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_auth = StellarBurgerApi.stellar_auth_user(random_user_data_for_registration)

        assert response_auth.status_code == 200 and response_auth.json()["success"] is True

    @allure.title('Проверка авторизации пользователя с несуществующим паролем и email')
    @allure.description('Проверка авторизации пользователя с указанием несуществующих email и пароля')
    def test_auth_user_with_incorrect_password_and_email(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        user_data = {
            "email": Helpers.generate_new_email(),
            "password": Helpers.generate_new_password()
        }
        response_auth = StellarBurgerApi.stellar_auth_user(user_data)

        assert response_auth.status_code == 401 and response_auth.json()["message"] == "email or password are incorrect"
