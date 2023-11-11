import os
import shutil
from datetime import datetime
import logging


def sort_photos_by_date(directory, time_step, log_file_path):
    # Создание логов отличается от модуля 1, здесь используется специальная библиотека
    logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s | %(message)s', encoding='utf-8')
    # Пустой словарь для трекинга созданных папок
    folders_created = {}
    # Обход всех файлов и поддиректорий в указанной директории
    for root, _, files in os.walk(directory):
        for file in files:
            # Формирование полного пути к файлу
            file_path = os.path.join(root, file)
            # Получение времени создания файла и преобразование формата в datetime
            file_creation_time = os.path.getctime(file_path)
            creation_date = datetime.fromtimestamp(file_creation_time)
            # Переменная для хранения подкаталога в зависимости от выбранного шага сортировки
            time_folder = ''
            if time_step == 'day':
                time_folder = creation_date.strftime("%Y/%m/%d")
            elif time_step == 'week':
                time_folder = creation_date.strftime("%Y/%U")
            elif time_step == 'month':
                time_folder = creation_date.strftime("%Y/%m")
            #     Создание пути к целевой папке, куда будет перемещен файл
            target_folder = os.path.join(directory, time_folder)

            # Проверка, создана ли папка для перемещения, если нет, создание
            if time_folder not in folders_created:
                os.makedirs(target_folder, exist_ok=True)
                folders_created[time_folder] = target_folder
            #     Перемещение в папку, запись результата в лог
            try:
                shutil.move(file_path, os.path.join(folders_created[time_folder], file))
                logging.info(f"Файл {file} перемещен в папку {folders_created[time_folder]}")
            except PermissionError:
                logging.error(f"Не удалось переместить файл {file}, так как он занят другим процессом")
