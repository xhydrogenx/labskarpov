import datetime
import hashlib
import os


async def find_and_remove_duplicates(directory: str, log_file: str):
    """Поиск файлов происходит по хэшу"""
    file_hashes = {}  # Словарь для хранения хешей

    with open(log_file, "a", encoding="utf-8") as log:
        # log.truncate(0)
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)  # Формирование полного пути к файлу
                with open(file_path, "rb") as f:
                    file_content = f.read()  # Чтение содержимого файла в бинарном режиме (по сути fopen(
                    # "filename.b", "rb"))
                    f.close()
                    file_hash = hashlib.md5(file_content).hexdigest()  # Подсчет хэша файла
                    if file_hash in file_hashes:
                        duplicate_path = file_hashes[file_hash]  # Если хэш уже есть в словаре - дубликат
                        current_time = datetime.datetime.now()
                        # Запись в лог файл
                        log.write(f"{current_time} | Дубликат найден: {file_path}, удален: {duplicate_path}\n")
                        try:
                            os.unlink(file_path)  # Удаление дубликата
                        except Exception as e:
                            log.write(f"Ошибка при удалении файла {file_path}: {e}\n")
                    else:
                        file_hashes[file_hash] = file_path  # Запись хэша файла в словаре (для последующего сравнения)

    return print("Поиск завершен. Дубликаты удалены, информация записана в файл.")
