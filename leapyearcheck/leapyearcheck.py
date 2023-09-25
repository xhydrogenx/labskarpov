import PySimpleGUI as sg

layout = [
    [sg.Text('Введите год', size=(25, 1), key='-text-', font='Helvetica 16')],
    [sg.InputText('', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
    [sg.Button('Проверить', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
    [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')]]

window = sg.Window('Проверка года на високосный', layout, size=(350, 350))

# year = int(input("Введите год: "))
# leap = 'Високосный'
# regular = 'Обычный'
#
# if year % 4 != 0:
#     print(regular)
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print(leap)
#     else:
#         print(regular)

# запускаем основной бесконечный цикл

while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
# закрываем окно и освобождаем используемые ресурсы
window.close()
