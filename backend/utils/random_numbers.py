import secrets
from typing import List


def generate_random_numbers(
    min_value: int,
    max_value: int,
    count: int = 1,
    unique: bool = True,
) -> List[int]:
    """
    Generate secure random numbers between min_value and max_value (inclusive).

    :param min_value: The minimum value of the range (inclusive).
    :param max_value: The maximum value of the range (inclusive).
    :param count: The number of random numbers to generate (default is 1).
    :param unique: Whether the generated numbers should be unique (default is True).
    :return: A list of random integers between min_value and max_value.
    """
    if min_value >= max_value:
        raise ValueError("min_value must be less than max_value")
    if unique and (max_value - min_value + 1) < count:
        raise ValueError("Range is too small to generate unique numbers")

    numbers = set() if unique else []
    while len(numbers) < count:
        random_number = secrets.randbelow(max_value - min_value + 1) + min_value
        if unique:
            numbers.add(random_number)
        else:
            numbers.append(random_number)

    return list(numbers)
