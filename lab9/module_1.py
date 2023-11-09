import os
import hashlib
import asyncio


async def find_and_remove_duplicates(directory: str, log_file: str):
    """Поиск файлов происходит по хэшу"""
    file_hashes = {}

    with open(log_file, "a", encoding="utf-8") as log:
        log.truncate(0)
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as f:
                    file_content = f.read()
                    f.close()
                    file_hash = hashlib.md5(file_content).hexdigest()
                    if file_hash in file_hashes:
                        duplicate_path = file_hashes[file_hash]
                        log.write(f"Дубликат найден: {file_path}, удален: {duplicate_path}\n")
                        try:
                            os.unlink(file_path)
                        except Exception as e:
                            log.write(f"Ошибка при удалении файла {file_path}: {e}\n")
                    else:
                        file_hashes[file_hash] = file_path

    return print("Поиск завершен. Дубликаты удалены, информация записана в файл.")
