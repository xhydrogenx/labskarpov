year = int(input("Введите год: "))
leap = 'Високосный'
regular = 'Обычный'

if year % 4 != 0:
    print(regular)
elif year % 100 == 0:
    if year % 400 == 0:
        print(leap)
    else:
        print(regular)
