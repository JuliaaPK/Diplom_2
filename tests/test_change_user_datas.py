import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestChangeUserInfo:
    @allure.title('Проверка изменения данных авторизованного пользователя')
    @allure.description('Проверка изменения полей email, password и name для авторизованного пользователя')
    def test_change_authorized_user_password_and_email(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        random_user_data_for_registration["email"] = Helpers.generate_new_email()
        random_user_data_for_registration["password"] = Helpers.generate_new_password()
        random_user_data_for_registration["name"] = Helpers.generate_new_name()

        response_update = StellarBurgerApi \
            .stellar_update_user_info(random_user_data_for_registration, response_access_token)

        assert response_update.status_code == 200 and response_update.json()["success"] is True

    @allure.title('Проверка изменения данных не авторизованного пользователя')
    @allure.description('Проверка изменения полей email, password и name для не авторизованного пользователя')
    def test_change_unauthorized_user_password_and_email(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        user_data = {
            "email": Helpers.generate_new_email(),
            "password": Helpers.generate_new_password(),
            "name": Helpers.generate_new_name()
        }
        response_update = StellarBurgerApi.stellar_update_user_info(user_data)

        assert response_update.status_code == 401 and response_update.json()["message"] == "You should be authorised"
