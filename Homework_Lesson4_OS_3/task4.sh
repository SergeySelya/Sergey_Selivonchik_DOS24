#!/bin/bash  

# редактируемая строка  
input_string="This is an example string for substring extraction."  

# диапазон изменяемого элемента подстроки
start=11  # начальная позиция для подстроки 
end=18    # конечная позиция для подстроки  

# опция удаления(true - все кроме диапазона, false - сам диапазон)
delete=false  

# Изменение строки в соотвествии с опцией и диапазоном подстроки 
if [ "$delete" = false ]; then  
    substring=$(echo "$input_string" | cut -c"$start"-"$end")  
    echo "Extracted substring: '$substring'"  
else  
    modified_string=$(echo "$input_string" | cut -c1-"$((start - 1))" && echo "$input_string" | cut -c"$((end + 1))"-)  
    echo "Modified string after deletion: '$modified_string'"  
fi  
