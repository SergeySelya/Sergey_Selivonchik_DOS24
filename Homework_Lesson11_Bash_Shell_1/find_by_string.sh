#!/bin/bash

# param1 - искомая строка в файлах
# param2 - каталог по которому будет идти поиск файлов
string=$1
catalog_name=$2

files=$(grep -rl "$string" "$catalog_name")

echo "Найденные файлы:"
for file in ${files[@]}; do
    file_size=$(wc -c "$file" | awk '{print $1}')
    echo "Файл: $file (Размер: $file_size байт)"
done

# вывод недоступных дирректорий
check_directories() {
  local dir=$catalog_name
  # Проверяем директорию
  if [ ! -r "$dir" ]; then
    echo "Недоступна для чтения: $dir"
  fi
  # Проходим по всем поддиректориям
  for subdir in "$dir"/*/; do
    # Проверяем, является ли элемент директорией
    if [ -d "$subdir" ]; then
      check_directories "$subdir"
    fi
  done
}
