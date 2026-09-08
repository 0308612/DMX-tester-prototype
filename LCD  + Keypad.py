import RPi.GPIO as GPIO
import time
from RPLCD.i2c import CharLCD
from time import sleep

lcd = CharLCD(i2c_expander='PCF8574',address=0x3f, port=1, cols=16, rows=2)

GPIO.setmode(GPIO.BCM)

Col_pins = [9, 22, 27, 17]
Row_pins = [16, 5, 6, 26]

KEYPAD_LAYOUT = [
     ["1","2","3","A"],
     ["4","5","6","B"],
     ["7","8","9","C"],
     ["*","0","*","D"]
]

for row in Row_pins:
     GPIO.setup(row, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

for col in Col_pins:
     GPIO.setup(col, GPIO.OUT)

def readLine(line, characters):
     GPIO.output(line, GPIO.HIGH)
     if(GPIO.input(Row_pins[0]) == 1):
          return(characters[0])
     if(GPIO.input(Row_pins[1]) == 1):
          return(characters[1])
     if(GPIO.input(Row_pins[2]) == 1):
          return(characters[2])
     if(GPIO.input(Row_pins[3]) == 1):
          return(characters[3])
     GPIO.output(line, GPIO.LOW)
                    
try:
     while True:
          key = readLine(None, None)
          if key is not None:
               lcd.cursor_pos = (1,4)
               lcd.write_string(f"[ {key} ]")
          time.sleep(0.1)

except KeyboardInterrupt:
     print("\ncleaning up")
     GPIO.cleanup()

