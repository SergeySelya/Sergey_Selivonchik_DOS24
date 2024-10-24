#!/bin/bash  

# Проверьте, передано ли правильное количество аргументов  
if [ "$#" -ne 2 ]; then  
    echo "Usage: $0 filename new_extension"  
    exit 1  
fi  

filename="$1"  
NEW_EXT="$2"  

# Проверка ,существует ли файл 
if [ ! -e "${filename}" ]; then  
    echo "File does not exist."  
    exit 1  
fi  

# Извлекаем текущее расширение  
CURRENT_EXT="${filename##*.}"  

# Проверка , на наличие расширения в исходном файле
if [ "$CURRENT_EXT" == "$filename" ]; then  
    echo "The file has no extension."  
else  
    # Меняем расширение файла 
    BASENAME="${filename%.*}"  
    mv "$filename" "$BASENAME.$NEW_EXT"  
    echo "File extension changed to .$NEW_EXT."  
fi  