from src.schemas.user import User


def test_getting_users_list(get_users):
    get_users.assert_status_code(200).validate(User)

