from backend.tests.config.config_random_generation import generate_random_number
from backend.tests.config.config_random_generation import generate_random_any_string
from backend.tests.config.config_random_generation import generate_random_upper_case
from backend.tests.config.config_random_generation import generate_random_lower_case
from backend.tests.config.config_random_generation import generate_random_special_char


def make_random_username():
    """Returns random string username"""

    random_user_name = (
        f'{generate_random_upper_case(8)}'
        f'{generate_random_lower_case(8)}'
    )

    return random_user_name


def make_random_first_name():
    """Returns random string first name"""

    random_first_name = (
        f'{generate_random_upper_case(8)}'
        f'{generate_random_lower_case(8)}'
    )

    return random_first_name


def make_random_last_name():
    """Returns random string last_name"""

    random_last_name = (
        f'{generate_random_upper_case(8)}'
        f'{generate_random_lower_case(8)}'
    )

    return random_last_name


def make_random_email():
    """Returns random string email"""

    random_email = (
        f'{generate_random_any_string(8)}'
        f'{generate_random_number(5)}@'
        f'{generate_random_lower_case(5)}.'
        f'{generate_random_lower_case(3)}'
    )

    return random_email


def make_random_password():
    """Returns random string password"""

    random_passwd = (f'{generate_random_special_char(8)}' 
                      f'{generate_random_any_string(8)}' 
                      f'{generate_random_number(10) * 25}')

    return random_passwd
