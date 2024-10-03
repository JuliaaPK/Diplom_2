import pytest

from helpers import Helpers


@pytest.fixture()
def random_user_data_for_registration():
    random_user_data = Helpers.create_random_user_data_for_registration()
    yield random_user_data
    Helpers.delete_user_if_exists(random_user_data)
