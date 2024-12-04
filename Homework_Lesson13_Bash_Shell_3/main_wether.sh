#!/bin/bash

source API_Call_Weather.sh
source Parser_API_Wether.sh

main_weather() {
    # Country Unit(imperial or metric) Lang
    CITY="Minsk"
    UNITS="m"
    LANG="en"
    COUNT_DAY=8

    api_call_wether $CITY $UNITS $LANG $COUNT_DAY

    parser_core_weather $UNITS
}

main_weather



