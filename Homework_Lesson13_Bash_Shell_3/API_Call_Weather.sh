#!/bin/bash

api_call_wether() {
    # bash main_weather.sh (city) (day4,16) (С,F) (lang)
    API_ID="baa12bb7d2ed31c6c4b31e8a5d40d726"
    CITY=$1
    UNITS=$2
    LANG=$3
    COUNT_DAY=$4
    

    # Units
    if [ $UNITS == "i" ]; then
        UNITS="imperial"
    elif [ $UNITS == "m" ]; then
        UNITS="metric"
    else
        echo -e "\nWarn: < ${UNITS} > is not exist you can chose: \n i-imperial \n m-metric\n * metric unit is default \n"
    fi

    # count day
    output=$(curl -X GET "https://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_ID&units=$UNITS&lang=$LANG&cnt=$COUNT_DAY")
    echo $output > weather.json
}