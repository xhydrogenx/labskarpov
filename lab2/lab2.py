from datetime import datetime


class Person:
    def __init__(self, first_name="", last_name="", birth_date=datetime(2000, 1, 1)):
        self._first_name = first_name
        self._last_name = last_name
        self._birth_date = birth_date

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def birth_date(self):
        return self._birth_date

    @birth_date.setter
    def birth_date(self, value):
        self._birth_date = value

    @property
    def birth_year(self):
        return self._birth_date.year

    @birth_year.setter
    def birth_year(self, value):
        self._birth_date = self._birth_date.replace(year=value)

    def ToFullString(self):
        return f"Имя: {self._first_name}, Фамилия: {self._last_name}, Дата рождения: {self._birth_date}"

    def ToShortString(self):
        return f"{self._first_name} {self._last_name}"


# Пример использования класса Person:
person = Person("Иван", "Карпов", datetime(1999, 12, 8))
print(person.ToFullString())  # Вывод полной информации
print(person.ToShortString())  # Вывод краткой информации (имя и фамилия)
print(person.birth_year)  # Вывод года рождения
person.birth_year = 1985  # Изменение года рождения
print(person.ToFullString())  # Вывод обновленной информации
