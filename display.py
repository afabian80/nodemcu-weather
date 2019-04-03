from tm1637 import TM1637
from machine import Pin
from utime import sleep_ms


class Display:
    display = None

    def __init__(self, clk_pin, dio_pin, brightness):
        self.display = TM1637(clk=Pin(clk_pin), dio=Pin(dio_pin))
        self.display.brightness(brightness)
        self.display.show('----')
        sleep_ms(100)

    def show(self, text):
        self.display.show(text)

    def number(self, num):
        self.display.number(num)
