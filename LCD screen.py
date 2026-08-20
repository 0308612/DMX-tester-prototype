from rpi_lcd import LCD
from time import sleep

lcd = LCD(0x3f, 1, 16, 2, True)

#lcd.text('hello world', 1, 'center')