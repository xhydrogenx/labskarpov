import pytest


def generate_first_n_letters(n):
    # n: Количество букв.
    # Возвращает: Строка.
    if not 1 <= n <= 26:
        raise ValueError("Число букв должно быть в диапазоне от 1 до 26")

    return "".join([chr(i + ord("A")) for i in range(n)])


class TestGenerateFirstNLetters(object):

    # Тестирование значений подходящих по условию
    def test_positive(self):
        assert generate_first_n_letters(1) == "A"
        assert generate_first_n_letters(5) == "ABCDE"
        assert generate_first_n_letters(26) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    #   Тестирование значений не подходящих по условию
    @pytest.mark.xfail(reason="Ожидается исключение ValueError", run=False, strict=True)
    def test_negative(self):
        with pytest.raises(ValueError):
            generate_first_n_letters(-1)
        with pytest.raises(ValueError):
            generate_first_n_letters(27)


if __name__ == "__main__":
    pytest.main()
