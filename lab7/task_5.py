import pytest


def sum_of_digits(s):
    try:
        return sum(int(digit) for digit in s if digit.isdigit())
    except ValueError:
        raise ValueError("Входными данными должна быть строка, представляющая положительное целое число.")


def test_valid_numbers():
    assert sum_of_digits("12345") == 15
    assert sum_of_digits("9876") == 30
    assert sum_of_digits("1001") == 2


def test_empty_string():
    assert sum_of_digits("") == 0


def test_non_numeric_characters():
    assert sum_of_digits("abc123") == 6
    assert sum_of_digits("12x34") == 10


def test_invalid_input():
    with pytest.raises(ValueError):
        sum_of_digits("123.45")
    with pytest.raises(ValueError):
        sum_of_digits("-123")


if __name__ == '__main__':
    pytest.main()
