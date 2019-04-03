from display import Display
from config import Config
from wifi import Wifi, WifiConnectError
from weather import Weather
from time import sleep


def log_error(e):
    with open('error.log', 'a') as f:
        f.write(e)


def main():
    display = None
    wifi = None
    weather = None
    try:
        display = Display(clk_pin=5, dio_pin=4, brightness=4)
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
        except Exception as e:
            print(e)
            display.show('E 19')
            log_error(e)
            break


if __name__ == '__main__':
    main()
