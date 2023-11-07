import pytest


# Основная функция проверки года на високосный год
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


# Функция подсчета количества дней в году
def days_in_year(year):
    if is_leap_year(year):
        return 366
    else:
        return 365


# Проверка подходящих значений
def test_valid_years():
    assert days_in_year(2000) == 366
    assert days_in_year(2024) == 366
    assert days_in_year(2022) == 365
    assert days_in_year(2100) == 365


# Проверка неправильных значений
def test_out_of_range_years():
    with pytest.raises(ValueError):
        days_in_year(0)
    with pytest.raises(ValueError):
        days_in_year(-2022)


# Проверка самой функции проверки на високосный год, насколько правильно она определяет високосный год или нет
def test_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(2024) == True
    assert is_leap_year(2022) == False
    assert is_leap_year(2100) == False


if __name__ == '__main__':
    pytest.main()
