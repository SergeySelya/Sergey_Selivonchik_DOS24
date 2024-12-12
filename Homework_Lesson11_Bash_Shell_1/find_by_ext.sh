#!/bin/bash

# param1 - Имя нового файла в который запишеться вывод скрипта
# param2 - каталог по которому будет идти поиск файлов
# param3 - искомое расширение файлов 

new_file=$1
catalog_name=$2
extention=$3

chmod +x create_test_file.sh
./create_test_file.sh "$catalog_name"

ls "$catalog_name" | grep "$extention" >> "$catalog_name/$new_file"
