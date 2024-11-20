#!/bin/bash
new_file=$1
catalog_name=$2
extention=$3

chmod +x create_test_file.sh
./create_test_file.sh "$catalog_name"

ls "$catalog_name" | grep "$extention" >> "$catalog_name/$new_file"
