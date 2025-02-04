import os

def list_directory_contents(path):
    # Проверяем, существует ли указанный путь
    if not os.path.exists(path):
        print(f"Путь '{path}' не существует.")
        return
    
    # Проверяем, является ли путь директорией
    if not os.path.isdir(path):
        print(f"Путь '{path}' не является директорией.")
        return
    
    # Проходим по всем директориям и файлам
    for root, dirs, files in os.walk(path):
        print(f"\nТекущая папка: {root}")
        
        # Сортировка папок и файлов по имени
        dirs.sort()
        files.sort()
        
        # Выводим папки и файлы
        print(f"Папки ({len(dirs)}): {dirs}")
        print(f"Файлы ({len(files)}): {files}")

# Запрос у пользователя пути к папке
folder_path = input("Введите путь к папке для обхода: ").strip()

# Вызов функции с указанным путём
list_directory_contents(folder_path)