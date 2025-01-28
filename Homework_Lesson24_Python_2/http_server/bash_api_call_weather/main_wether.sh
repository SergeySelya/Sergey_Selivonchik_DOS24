#!/bin/bash

parser_core_weather() {
    UNITS="F"
    if [ $1 == "metric" ]; then
        UNITS="°C"
    fi

    country=$(jq '.sys .country' ./weather.json)
    city=$(jq '.name' ./weather.json)
    description=$(jq '.weather .[] .description' ./weather.json)
    temp_min=$(jq '.main .temp_min' ./weather.json)
    temp_max=$(jq '.main .temp_max' ./weather.json)
    pressure=$(jq '.main .pressure' ./weather.json)
    speed=$(jq '.wind .speed' ./weather.json)
    date=$(jq '.dt' ./weather.json)
    sunrise=$(jq '.sys .sunrise' ./weather.json)
    sunset=$(jq '.sys .sunset' ./weather.json)
    
    alert=$($whitelist | jq -r '.[].alertName')
    echo "
    country: $country
    city: $city
    description: $description
    temp_min: $temp_min $UNITS
    temp_max: $temp_max $UNITS
    pressure: $pressure in
    speed of the wind: $speed m/s
    $sunrise
    sunrise: $(date -d @$sunrise)
    sunset: $(date -d @$sunset)
    date: $(date -d @$date)
    "
}

#!/bin/bash

api_call_wether() {
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

    output=$(curl -X GET -s "https://api.openweathermap.org/data/2.5/weather?q=$CITY&appid=$API_ID&units=$UNITS&lang=$LANG&cnt=$COUNT_DAY")
    echo $output > weather.json
}


main_weather() {
    # Country Unit(imperial or metric) Lang
    # Принимаем аргументы
    CITY=$1
    UNITS=$2
    LANG=$3
    COUNT_DAY=$4


    api_call_wether $CITY $UNITS $LANG $COUNT_DAY

    parser_core_weather $UNITS

    rm weather.json
}

main_weather "$1" "$2" "$3" "$4"



