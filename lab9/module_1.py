import os
import hashlib
import asyncio


async def find_and_remove_duplicates(directory):
    """Поиск файлов происходит по хэшу"""
    file_hashes = {}

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                file_content = f.read()
                f.close()
                file_hash = hashlib.md5(file_content).hexdigest()
                if file_hash in file_hashes:
                    # Этот файл - дубликат
                    print(f"Дубликат найден: {file_path}")
                    try:
                        os.unlink(file_path)
                    except PermissionError as e:
                        print(f"Ошибка при удалении файла {file_path}: {e}")
                else:
                    file_hashes[file_hash] = file_path
    return print("Дубликатов не найдено")
