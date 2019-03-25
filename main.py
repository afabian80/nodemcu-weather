import tm1637
from machine import Pin
import urequests as requests
import json
import time
import os

tm = tm1637.TM1637(clk=Pin(5), dio=Pin(4))
url = 'http://api.openweathermap.org/data/2.5/weather?q={0}&APPID={1}'
kelvin = 273.15

while True:
    try:
        f = open('api.key', 'r')
        api_key = f.readline()
        f.close()
        f = open('location.txt', 'r')
        location = f.readline()
        f.close()
        resp = requests.get(url.format(location, api_key))
        data = json.loads(resp.text)
        temp_fine = float(data['main']['temp']) - kelvin
        temp = round(temp_fine)
        tm.brightness(3)
        tm.number(temp)
    except ValueError:
        tm.show('er 1')
    except NameError:
        tm.show('er 2')
    except TypeError:
        tm.show('er 3')
    except IOError:
        tm.show('er 4')
    except:
        tm.show('er 0')

    time.sleep(600)
    tm.show('----')
    time.sleep(1)
