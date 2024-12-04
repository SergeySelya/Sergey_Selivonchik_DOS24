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
    sunrise: $(date -r $sunrise)
    sunset: $(date -r $sunset)
    date: $(date -r $date)
    "
}

