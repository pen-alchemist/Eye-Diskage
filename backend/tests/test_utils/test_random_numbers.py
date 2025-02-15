import pytest

from backend.utils.random_numbers import generate_random_numbers


def test_generate_single_random_number_length():
    """Test generating a single random number."""
    result = generate_random_numbers(1, 10)
    assert len(result) == 1

def test_generate_single_random_number_range():
    """Test that a single random number is within the valid range."""
    result = generate_random_numbers(1, 10)
    assert 1 <= result[0] <= 10

def test_generate_multiple_random_numbers_length():
    """Test generating multiple random numbers."""
    result = generate_random_numbers(1, 10, count=5)
    assert len(result) == 5

def test_generate_multiple_random_numbers_range():
    """Test that multiple random numbers are within the valid range."""
    result = generate_random_numbers(1, 10, count=5)
    for num in result:
        assert 1 <= num <= 10

def test_generate_unique_random_numbers_length():
    """Test generating multiple unique random numbers."""
    result = generate_random_numbers(1, 10, count=5, unique=True)
    assert len(result) == 5

def test_generate_unique_random_numbers_uniqueness():
    """Test that multiple random numbers are unique."""
    result = generate_random_numbers(1, 10, count=5, unique=True)
    assert len(set(result)) == 5

def test_generate_unique_random_numbers_range():
    """Test that unique random numbers are within the valid range."""
    result = generate_random_numbers(1, 10, count=5, unique=True)
    for num in result:
        assert 1 <= num <= 10

def test_generate_non_unique_random_numbers_length():
    """Test generating multiple non-unique random numbers."""
    result = generate_random_numbers(1, 10, count=5, unique=False)
    assert len(result) == 5

def test_generate_non_unique_random_numbers_range():
    """Test that non-unique random numbers are within the valid range."""
    result = generate_random_numbers(1, 10, count=5, unique=False)
    for num in result:
        assert 1 <= num <= 10

def test_generate_random_numbers_with_min_equal_max():
    """Test generating random numbers when min_value equals max_value."""
    with pytest.raises(ValueError):
        generate_random_numbers(5, 5, count=3)

def test_generate_random_numbers_with_invalid_range():
    """Test generating random numbers with an invalid range (min_value > max_value)."""
    with pytest.raises(ValueError):
        generate_random_numbers(10, 1)

def test_generate_random_numbers_with_insufficient_range_for_unique():
    """Test generating unique random numbers with a range smaller than the count."""
    with pytest.raises(ValueError):
        generate_random_numbers(1, 5, count=10, unique=True)

def test_generate_random_numbers_with_zero_count():
    """Test generating random numbers with a count of 0."""
    result = generate_random_numbers(1, 10, count=0)
    assert result == []

def test_generate_random_numbers_with_negative_count():
    """Test generating random numbers with a negative count."""
    with pytest.raises(TypeError):
        generate_random_numbers(1, '*&$&#*$#&&*#$', count=-1)

def test_generate_random_numbers_with_large_range_length():
    """Test generating random numbers with a large range."""
    result = generate_random_numbers(1, 1000000, count=10)
    assert len(result) == 10

def test_generate_random_numbers_with_large_range_range():
    """Test that random numbers with a large range are within the valid range."""
    result = generate_random_numbers(1, 1000000, count=10)
    for num in result:
        assert 1 <= num <= 1000000

def test_generate_random_numbers_with_negative_range_length():
    """Test generating random numbers with a negative range."""
    result = generate_random_numbers(-10, -1, count=5)
    assert len(result) == 5

def test_generate_random_numbers_with_negative_range_range():
    """Test that random numbers with a negative range are within the valid range."""
    result = generate_random_numbers(-10, -1, count=5)
    for num in result:
        assert -10 <= num <= -1

def test_generate_random_numbers_with_large_count_length():
    """Test generating a large number of random numbers."""
    result = generate_random_numbers(1, 100, count=1000, unique=False)
    assert len(result) == 1000

def test_generate_random_numbers_with_large_count_range():
    """Test that a large number of random numbers are within the valid range."""
    result = generate_random_numbers(1, 100, count=1000, unique=False)
    for num in result:
        assert 1 <= num <= 100
