# nodemcu-weather
Micropython application to show the current temperature from openweathermap on a TM1637 LED display

# Hardware Requirements
1. Any kind of ESP8266 board that is supported by micropython. Mine is a nodeMCU v0.9

    Discuss http://docs.micropython.org/en/latest/
1. Any computer with USB and Python installed
1. A TM1637 display (https://playground.arduino.cc/Main/TM1637/)
1. Make the following wired connections
    - Display Ground pin to ESP8266 board Ground
    - Display Vcc pin to ESP8266 board +3V
    - Display DIO pin to ESP8266 board GPIO 4 (D2 pin on my NodeMCU)
    - Display CLK pin to ESP8266 board GPIO 5 (D1 pin on my NodeMCU)
    
    Note: 
    - The pin labels on your board may be different. Check the docs.
    - You can update the pins used in the main.py file (__tm1637.TM1637(...)__)

# Software Requirements
1. Install __ampy__ from https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy
    
    Example:
    ```
    sudo pip install adafruit-ampy
    ```
1. Register a free account at https://openweathermap.org/
1. Obtain your API key at https://home.openweathermap.org/api_keys
1. Save your API key in file called __api.key__

    Example content:
    ```
    1234567890abcdefghijkl1234567890
    ```
1. Save your location data in a file called __location.txt__

    Example content:
    ```
    Budapest,hu
    ```
1. Save your wifi access info in a file called __wifi.secret__
    
    Example content:
    ```
    MYSSID
    MyPassword
    ```

    *Note*: password has to be saved in plain text, but you will only copy it to the ESP8266 board later, nowhere else.
1. Connect the ESP8266 board to your computer via USB, and find out its device name.

    Example:
    ```
    ls /dev/ttyUSB*
    ```
    For example, my board is /dev/ttyUSB0
1. Upload all the files
    ```
    ampy -p /dev/ttyUSB0 put boot.py
    ampy -p /dev/ttyUSB0 put main.py
    ampy -p /dev/ttyUSB0 put api.key
    ampy -p /dev/ttyUSB0 put location.txt
    ampy -p /dev/ttyUSB0 put wifi.secret
    ampy -p /dev/ttyUSB0 put tm1637.py
    ampy -p /dev/ttyUSB0 put urequests.py
    ```

# Usage
1. Unplug the ESP8266 board from the power source and then re-connect it
1. Your device should show the current temperature on the display

# Troubleshooting
1. If the display is still dark, it means it could not connect to the wifi

    Further docs: http://docs.micropython.org/en/latest/esp8266/quickref.html#installing-micropython
1. If you have error messages on the display, your api key or location files may be incorrect
1. You can connect to an interactive Python REPL on the board via USB
    ```
    picocom /dev/ttyUSB0 -b115200
    ```
1. You can connect wirelessly via webrepl: 

    More details at https://learn.adafruit.com/micropython-basics-esp8266-webrepl/access-webrepl
    
    Note: Board access point feature is currently disabled in the boot.py file with ```ap_if.active(False)```. You can remove it to play with it.

    Connect to __ws://192.168.xxx.yyy:8266/__
    
    Find out the IP address by checking out the dhcp client list on your router.
