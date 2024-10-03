import requests

from Urls import Urls


class StellarBurgerApi:
    @staticmethod
    def stellar_registration_user(user_data):
        return requests.post(Urls.USER_CREATION, json=user_data)

    @staticmethod
    def stellar_auth_user(user_data):
        return requests.post(Urls.USER_AUTH, json=user_data)

    @staticmethod
    def stellar_delete_user(user_access_token):
        return requests.delete(Urls.USER_DELETE, headers={'Authorization': user_access_token})

    @staticmethod
    def stellar_update_user_info(user_data, access_token=None):
        return requests.patch(
            Urls.USER_GET_OR_UPDATE_INFO,
            headers={'Authorization': access_token} if access_token is not None else None,
            json=user_data
        )

    @staticmethod
    def get_all_available_ingredients():
        return requests.get(Urls.GET_INGREDIENTS_DATA)

    @staticmethod
    def stellar_create_order(ingredients, access_token=None):
        return requests.post(
            Urls.ORDER_CREATION_AND_GET_INFO,
            headers={'Authorization': access_token} if access_token is not None else None,
            json={"ingredients": ingredients}
        )

    @staticmethod
    def stellar_get_user_orders(access_token=None):
        return requests.get(
            Urls.ORDER_CREATION_AND_GET_INFO,
            headers={'Authorization': access_token} if access_token is not None else None
        )
