from backend.tests.config.config_random_generation import generate_random_number
from backend.tests.config.config_random_generation import generate_random_any_string
from backend.tests.config.config_random_generation import generate_random_upper_case
from backend.tests.config.config_random_generation import generate_random_lower_case
from backend.tests.config.config_random_generation import generate_random_special_char


def make_random_string(border_value):
    """Returns string with any string, number, upper_case, special char
    using border number (value) that is len of string"""

    number_len = border_value // 5

    random_string = (
        f'{generate_random_number(number_len)}'
        f'{generate_random_any_string(number_len)}'
        f'{generate_random_upper_case(number_len)}.'
        f'{generate_random_lower_case(number_len)}'
        f'{generate_random_special_char(number_len)}'
    )

    return random_string


def random_string_no_special_char(border_value):
    """Returns string with any string, number, upper_case, special char
    using border number (value) that is len of string"""

    number_len = border_value // 4

    random_string = (
        f'{generate_random_number(number_len)}'
        f'{generate_random_any_string(number_len)}'
        f'{generate_random_upper_case(number_len)}.'
        f'{generate_random_lower_case(number_len)}'
    )

    return random_string
