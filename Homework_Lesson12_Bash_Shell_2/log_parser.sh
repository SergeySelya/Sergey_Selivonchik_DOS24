#!/bin/bash

# generate log
bash ./generate_log.sh

# logs parser
result=$(grep "403$" ./server.log)
IFS=$'\n'

for line in $result; do
    IFS=$' ' read -ra array <<< $line
    usernames+=(${array[3]})
    ip_all+=(${array[4]})
done

# Output IP
echo -e "\nSuccessful logins (IP addresses):"
for ip in "${ip_all[@]}"; do  
    echo "$ip" | cut -c 4-
done  

# Output Username
echo -e "\nUsers with failed logins:"
for name in "${usernames[@]}"; do  
    echo "$name" | cut -c 6-
done  
