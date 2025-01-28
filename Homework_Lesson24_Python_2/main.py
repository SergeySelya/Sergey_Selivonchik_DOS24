
## ЗАДАНИЕ Jun Python

# 1. **Проверка доступности IP-адресов:**
# - Напишите скрипт, который принимает на вход список IP-адресов и проверяет их доступность с помощью ping-запросов. Результаты проверки должны сохраняться в отдельный файл.
import subprocess
import platform

def check_ip(ip_list):
   # Определяем команду для ping в зависимости от операционной системы
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    for ip in ip_list:
        
        command = ["ping", param, "1", ip]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.returncode == 0:
            print(f"{ip} доступен.")
        else:
            print(f"{ip} недоступен.") 
            
# ВЫЗОВ ЗАДАНИЕ 1
'''
ip_list = ["172.67.181.116","47.214.112.36","45.12.31.147"]
check_ip(ip_list)
'''

#2. **Уникальность элементов в кортеже:**
#- Напишите скрипт, который принимает на вход кортеж и проверяет, все ли его элементы являются уникальными.

def check_tuple(my_tuple):
    # Сравниваем длину множества и длину кортежа
    return "уникальный" if len(my_tuple) == len(set(my_tuple)) else "неуникальный"

# ВЫЗОВ ЗАДАНИЕ 2
'''
print(check_tuple((1, 2, 3, 4)))  # "уникальный"
print(check_tuple((1, 2, 3, 3)))  # "неуникальный"
'''


#3. **Поиск файлов по подстроке:**
#- Напишите скрипт, который принимает на вход список файлов и находит те, имена которых содержат определённую подстроку.
import os

def find_my_str(filename_list):
    result = []
    
    for filename in filename_list:
        with open(filename, 'r') as file:
            for line in file:
                if "Hello" in line:
                    result.append(filename)

    return result

# ВЫЗОВ ЗАДАНИЕ 3
'''
with open("file1.txt", 'w') as file1:
    file1.write("Это первый файл.")
with open("file2.txt", 'w') as file2:
    file2.write("Это второй файл.\nHello")
print("\n1) Файлы 'file1.txt', 'file2.txt' , успешно созданы и строка 'hello' добавлена в file2.txt.\n")

filename_list = ['file1.txt', 'file2.txt']
print('2) Имя файла в котором найдена подстрока "Hello" ')
print(find_my_str(filename_list))      
os.remove('file1.txt')            
os.remove('file2.txt')         
print("\n3) Файлы 'file1.txt', 'file2.txt' , успешно удалены\n ")
'''

#4. **Общие символы в строках:**
#- Напишите скрипт, который принимает на вход две строки и выводит на экран все символы, которые встречаются в обеих строках.
def find_common_symb(list_mystr):
    set1 = set(list(list_mystr[0]))
    set2 = set(list(list_mystr[1]))
    result = set1 & set2
    return result
    
# ВЫЗОВ ЗАДАНИЕ 4
'''
list_mystr = ['abb cd', 'vbmva']
print('Cписов общих элементов')
print(find_common_symb(list_mystr))
'''
    
#6. **Замена гласных в строке:**
#- Напишите скрипт, который принимает на вход строку и заменяет в ней все гласные буквы на символ "-".

def replace_letters(my_str):
    my_str = list(my_str)
    vowels = "аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU"
    result = list(map(lambda x: x if x not in vowels else '-', my_str))
    result = " ".join(result)
    return result

# ВЫЗОВ ЗАДАНИЕ 5
'''
my_str = 'Привет меня зовут Сергей'
print(f'\nИсходная строк\n{my_str} \n\nПреобразованная:')
print(replace_letters(my_str))
'''

