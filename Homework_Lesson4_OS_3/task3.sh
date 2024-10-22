#!/bin/bash  

# Check if the right number of arguments are passed  
if [ "$#" -ne 2 ]; then  
    echo "Usage: $0 filename new_extension"  
    exit 1  
fi  

filename="$1"  
NEW_EXT="$2"  

# Check if the file exists  
if [ ! -e "${filename}" ]; then  
    echo "File does not exist."  
    exit 1  
fi  

# Extract the current extension  
CURRENT_EXT="${filename##*.}"  

# Check if the current extension is the same as the filename (indicating no extension)  
if [ "$CURRENT_EXT" == "$filename" ]; then  
    echo "The file has no extension."  
else  
    # Rename file with new extension  
    BASENAME="${filename%.*}"  
    mv "$filename" "$BASENAME.$NEW_EXT"  
    echo "File extension changed to .$NEW_EXT."  
fi  