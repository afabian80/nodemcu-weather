from display_tm137 import DisplayTm
from display_max7219 import DisplayMax
from config import Config
from wifi import Wifi, WifiConnectError
from weather import Weather, WeatherUpdateError
from time import sleep


def log_error(e):
    with open('error.log', 'a') as f:
        f.write(e)


def main():
    display = None
    wifi = None
    weather = None
    try:
        # display = DisplayTm(clk_pin=5, dio_pin=4, brightness=4)
        display = DisplayMax(sck_pin=14, mosi_pin=13, miso_pin=12, ss_pin=16, brightness=15)
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
