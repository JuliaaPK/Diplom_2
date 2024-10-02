import allure

from helpers import Helpers
from stellar_burger_api import StellarBurgerApi


class TestCreateOrder:
    @allure.title('Проверка создание заказа авторизованного пользователя с ингредиентами')
    @allure.description('Проверка создания заказа для авторизованного пользователя с указанием ингредиентов')
    def test_create_order_with_auth_and_ingredients(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        list_of_ingredients = Helpers.get_hash_list_of_n_first_ingredients(2)
        response_order = StellarBurgerApi.stellar_create_order(list_of_ingredients, response_access_token)

        assert response_order.status_code == 200 and response_order.json()["success"] is True

    @allure.title('Проверка создание заказа не авторизованного пользователя с ингредиентами')
    @allure.description('Проверка создания заказа для не авторизованного пользователя с указанием ингредиентов')
    def test_create_order_without_auth_but_with_ingredients(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        list_of_ingredients = Helpers.get_hash_list_of_n_first_ingredients(2)
        response_order = StellarBurgerApi.stellar_create_order(list_of_ingredients)

        assert response_order.status_code == 200 and response_order.json()["success"] is True

    @allure.title('Проверка создание заказа авторизованного пользователя без ингредиентов')
    @allure.description('Проверка создания заказа для авторизованного пользователя без указания ингредиентов')
    def test_create_order_with_auth_but_without_ingredients(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_access_token = Helpers.get_user_access_token(random_user_data_for_registration)
        list_of_ingredients = []
        response_order = StellarBurgerApi.stellar_create_order(list_of_ingredients, response_access_token)

        assert response_order.status_code == 400 \
               and response_order.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверка создание заказа не авторизованного пользователя без ингредиентов')
    @allure.description('Проверка создания заказа для не авторизованного пользователя без указания ингредиентов')
    def test_create_order_without_auth_and_ingredients(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        list_of_ingredients = []
        response_order = StellarBurgerApi.stellar_create_order(list_of_ingredients)

        assert response_order.status_code == 400 \
               and response_order.json()["message"] == "Ingredient ids must be provided"

    @allure.title('Проверка создание заказа авторизованного пользователя с несуществующим hash')
    @allure.description(
        'Проверка создания заказа для авторизованного пользователя с указанием несуществующих hash ингредиентов')
    def test_create_order_with_auth_and_incorrect_ingredient_hash(self, random_user_data_for_registration):
        StellarBurgerApi.stellar_registration_user(random_user_data_for_registration)
        response_order = StellarBurgerApi.stellar_create_order(Helpers.create_list_with_fake_hash_ingredients(2))

        assert response_order.status_code == 500
