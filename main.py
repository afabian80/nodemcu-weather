from display_tm137 import DisplayTm
from display_max7219 import DisplayMax
from config import Config
from wifi import Wifi, WifiConnectError
from weather import Weather, WeatherUpdateError
from time import sleep
from machine import ADC


def log_error(e):
    with open('error.log', 'a') as f:
        f.write(e)


def map_value(x, in_min, in_max, out_min, out_max):
    if x < in_min:
        x = in_min
    if x > in_max:
        x = in_max
    return round((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)


def adc_read_oversample(adc_instance, samples):
    value = 0
    for i in range(0, samples):
        value += (adc_instance.read() / samples)
    return round(value)


def main():
    display = None
    wifi = None
    weather = None
    adc = ADC(0)
    try:
        display = DisplayMax(sck_pin=14, mosi_pin=13, miso_pin=12, ss_pin=16, brightness=15)
        display.set_brightness(map_value(adc_read_oversample(adc, 32), 50, 1024, 0, 15))
        config = Config(file_name='config.json')
        weather = Weather(api_key=config.api_key, location=config.location)
        wifi = Wifi(config.wifi_ssid, config.wifi_password)
    except OSError as e:
        print(e)
        display.show('E 01')
        log_error(e)
        return
    except KeyError as e:
        print(e)
        display.show('E 02')
        log_error(e)
        return
    except Exception as e:
        print(e)
        display.show('E 09')
        log_error(e)
        return

    while True:
        try:
            if not wifi.is_connected():
                wifi.connect()
            weather.update()
            display.set_brightness(map_value(adc_read_oversample(adc, 32), 50, 1024, 0, 15))
            display.number(weather.temperature)
            sleep(60)
            display.show('UP  ')
            sleep(1)
        except WifiConnectError as e:
            print(e)
            display.show('E 11')
            sleep(10)
        except WeatherUpdateError as e:
            print(e)
            display.show('E 12')
            sleep(10)
        except Exception as e:
            print(e)
            display.show('E 19')
            log_error(e)
            break


if __name__ == '__main__':
    main()
