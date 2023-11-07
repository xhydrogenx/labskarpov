import pytest
import re


# Основная функция проверки почты
def is_valid_email(email: str):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))  # Преобразование в булево значение для проверки на истину


# Проверка подходящих значений
def test_valid_emails():
    assert is_valid_email("test@test.com") == True
    assert is_valid_email("user@example.co.uk") == True
    assert is_valid_email("user1234@example1234.com") == True


# Проверка неправильных значений
def test_invalid_emails():
    assert is_valid_email("invalid_email") == False
    assert is_valid_email("test@.com") == False
    assert is_valid_email("@example.com") == False


# Дополнительные варианты проверки, для адресов с числами и символами
def test_valid_email_with_numbers():
    assert is_valid_email("user1234@example.com") == True
    assert is_valid_email("john.doe1234@gmail.com") == True


def test_valid_email_with_special_characters():
    assert is_valid_email("alice.doe@example.co.uk") == True


if __name__ == '__main__':
    pytest.main()
