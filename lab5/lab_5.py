import re

regexs_dict = {
    'a': r'^a$',
    'aaaaaa': r'^a{6}$',
    'a aa a': r'^(a\s+)+a$',
    '5symbols': r'^[a-zA-Z0-9]{5,}$',
    'mail': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'street': r'^ул\.\s+([^д]+)\s+д\.\s+(\d+/\d+)$'
}

test_data = ["a",
             "aaaaaa",
             "a aa a",
             "b",
             "a a a a",
             "ababa",
             "aaaaab",
             "a1a2a3a4",
             "aa a a",
             "abcde",
             "12345",
             "a1b2c3",
             "ab",
             "abcdefg",
             "1234567",
             "a1",
             "a12bc",
             "1a2b3c",
             "test@test.test",
             "user@example.com",
             "12345@gmail.com",
             "invalid.email",
             "john.doe@subdomain.co",
             "name.lastname@email.org",
             "another.email@sub.subdomain.info",
             "noat.com",
             "email@example",
             "ул. Примерная д. 10/5",
             "ул. Главная д. 25/1",
             "Неверный формат адреса",
             "ул. Пушкина д. 5/2",
             "ул. Ленина д. 15/10",
             "ул. Маяковского д. 7/3",
             "ул. Советская д. 50/5",
             "ул. Садовая д. 12/1",
             "ул. Жукова д. 30/4"]

for pattern_name, pattern in regexs_dict.items():
    print(f"Проверка паттерна '{pattern_name}':")
    for item in test_data:
        match = re.match(pattern, item)
        if match:
            print(f"Совпадение для строки '{item}': {match.group()}")
