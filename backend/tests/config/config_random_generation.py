import string
import secrets


def generate_random_number(upper_value):
    """Returns random number using upper value"""

    number_output = secrets.randbelow(upper_value)

    return number_output


def generate_random_any_string(iteration):
    """Returns random ascii letters using iteration"""

    letters = string.ascii_letters
    string_output = ''.join(secrets.choice(letters) for i in range(iteration))

    return string_output


def generate_random_upper_case(iteration):
    """Returns random upper case string using iteration"""

    letters = string.ascii_uppercase
    string_output = ''.join(secrets.choice(letters) for index in range(iteration))

    return string_output


def generate_random_lower_case(iteration):
    """Returns random lower case string using iteration"""

    letters = string.ascii_lowercase
    string_output = ''.join(secrets.choice(letters) for index in range(iteration))

    return string_output


def generate_random_special_char(iteration):
    """Returns random special symbols string using iteration"""

    special_characters = [char for char in '!@#$%^&*()_+-={}|":<>/?\\']
    char_output = ''.join(secrets.choice(special_characters) for index in range(iteration))

    return char_output
