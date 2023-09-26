import PySimpleGUI as sg

layout = [
    [sg.Text('Введите год', size=(25, 1), key='-text-', font='Helvetica 16')],
    [sg.InputText('', enable_events=True, key='-INPUT-', font='Helvetica 16')],
    [sg.Button('Проверить', enable_events=True, key='-FUNCTION-', font='Helvetica 16')],
    [sg.Text('Результат:', size=(25, 1), key='-text-', font='Helvetica 16')],
    [sg.Output(size=(80, 20))]
    ]

window = sg.Window('Проверка года на високосный', layout, size=(350, 350))


def year_check():
    print(values)
    # берем строку по ключу и преобразуем в число
    year = int(values['-INPUT-'])
    leap = 'Високосный'
    regular = 'Обычный'

    # 2 условия
    if year % 4 == 0 or (year % 100 != 0 and year % 400 == 0):
        print(leap)
    else:
        print(regular)


while True:
    # получаем события, произошедшие в окне
    event, values = window.read()
    # если отдает function - запустить функцию year_check
    if event == '-FUNCTION-':
        year_check()
    # если нажали на крестик
    if event in (sg.WIN_CLOSED, 'Exit'):
        # выходим из цикла
        break
# закрываем окно и освобождаем используемые ресурсы
window.close()
