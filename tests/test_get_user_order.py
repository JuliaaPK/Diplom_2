import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestGetUserOrder:
    @allure.title('Проверка получения заказов авторизованного пользователя')
    @allure.description('Проверка получения списка заказов для авторизованного в системе пользователя')
    def test_get_user_order_with_auth(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        list_of_ingredients = Helpers.get_hash_list_of_n_first_ingredients(2)
        StellarBurgerApi.stellar_create_order(list_of_ingredients, response_access_token)
        response_user_order = StellarBurgerApi.stellar_get_user_orders(response_access_token)

        assert response_user_order.status_code == 200 and response_user_order.json()["success"] is True

    @allure.title('Проверка получения заказов не авторизованного пользователя')
    @allure.description('Проверка получения списка заказов для не авторизованного в системе пользователя')
    def test_get_user_order_without_auth(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        list_of_ingredients = Helpers.get_hash_list_of_n_first_ingredients(2)
        StellarBurgerApi.stellar_create_order(list_of_ingredients, response_access_token)
        response_user_order = StellarBurgerApi.stellar_get_user_orders()

        assert response_user_order.status_code == 401 and response_user_order.json()[
            "message"] == "You should be authorised"
