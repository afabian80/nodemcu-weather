import max7219_4digit
from machine import Pin, SPI
from utime import sleep_ms


class DisplayMax:
    display = None

    def __init__(self, sck_pin, mosi_pin, miso_pin, ss_pin, brightness):
        spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=Pin(sck_pin), mosi=Pin(mosi_pin), miso=Pin(miso_pin))
        ss = Pin(ss_pin, Pin.OUT)
        self.display = max7219_4digit.Display(spi, ss, brightness)
        self.display.write_to_buffer('----');
        self.display.display()
        sleep_ms(100)

    def show(self, text):
        text = "{:>4}".format(text)
        self.display.write_to_buffer(text);
        self.display.display()

    def number(self, num):
        self.show(num)
