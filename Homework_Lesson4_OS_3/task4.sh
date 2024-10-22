#!/bin/bash  

# Input string  
input_string="This is an example string for substring extraction."  

# Character boundaries  
start=11  # starting position for substring (1-based index)  
end=18    # ending position for substring (1-based index)  

# Option to delete the substring (true/false)  
delete=false  

# Extracting the substring  
if [ "$delete" = false ]; then  
    substring=$(echo "$input_string" | cut -c"$start"-"$end")  
    echo "Extracted substring: '$substring'"  
else  
    modified_string=$(echo "$input_string" | cut -c1-"$((start - 1))" && echo "$input_string" | cut -c"$((end + 1))"-)  
    echo "Modified string after deletion: '$modified_string'"  
fi  
