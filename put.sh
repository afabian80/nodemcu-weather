#!/bin/bash

function put_all() {
    for f in boot.py config.json config.py display.py main.py tm1637.py urequests.py weather.py wifi.py
    do
        echo "Putting ${f}..."
        ampy -p /dev/ttyUSB0 put ${f}
    done
}

if [[ $# -eq 0 ]]
  then
    echo "Usage: put.sh (filename | all)"
    exit 1
fi

if [[ "$1" == "all" ]]
    then
        put_all
else
    echo "Putting ${1}..."
    ampy -p /dev/ttyUSB0 put $1
fi