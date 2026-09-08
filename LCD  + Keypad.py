import RPi.GPIO as GPIO
import time
from rpi_lcd import LCD

lcd = LCD(0x3f, 1, 16, 2, True)

GPIO.setmode(GPIO.BCM)

Col_pins = [9, 22, 27, 17]
Row_pins = [16, 5, 6, 26]

Keypad_Pressed = -1
Input = ""

for row in Row_pins:
     GPIO.setup(row, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

for col in Col_pins:
     GPIO.setup(col, GPIO.OUT)

def keypadCallback(channel):
     global Keypad_Pressed
     if Keypad_Pressed == -1:
          Keypad_Pressed = channel

GPIO.add_event_detect(Row_pins[0], GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(Row_pins[1], GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(Row_pins[2], GPIO.RISING, callback=keypadCallback)
GPIO.add_event_detect(Row_pins[3], GPIO.RISING, callback=keypadCallback)

def setAllLines(state):
     GPIO.output(Col_pins[0], state)
     GPIO.output(Col_pins[1], state)
     GPIO.output(Col_pins[2], state)
     GPIO.output(Col_pins[3], state)

def checkSpecialKeys():
     global Input
     pressed = False

     GPIO.output(Col_pins[3], GPIO.HIGH)

     if GPIO.input(Row_pins[2]) == 1:
          print("entered")
          pressed = True

     if not pressed and GPIO.input(Row_pins[0]) == 1:
          print("input reset")
          pressed = True

     GPIO.output(Col_pins[3], GPIO.LOW)

     if pressed:
          Input = ""


     return pressed

def readLine(line, characters):
     global Input

     GPIO.output(line, GPIO.HIGH)
     if GPIO.input(Row_pins[0]) == 1:
          Input = Input + characters[0]
     if GPIO.input(Row_pins[1]) == 1:
          Input = Input + characters[1]
     if GPIO.input(Row_pins[2]) == 1:
          Input = Input + characters[2]
     if GPIO.input(Row_pins[3]) == 1:
          Input = Input + characters[3]
     GPIO.output(line, GPIO.LOW)

try:
     while True:
          if Keypad_Pressed != -1:
               setAllLines(GPIO.HIGH)
               if GPIO.input(Keypad_Pressed) == 0:
                    Keypad_Pressed = -1
               else:
                    time.sleep(0.1)
          else:
               if not checkSpecialKeys():
                    readLine(Col_pins[0], ["1","2","3","A"])
                    readLine(Col_pins[1], ["4","5","6","B"])
                    readLine(Col_pins[2], ["7","8","9","C"])
                    readLine(Col_pins[3], ["*","0","#","D"])
                    time.sleep(0.1)
               else:
                    time.sleep(0.1)
          
except KeyboardInterrupt:
     print("\ncleaning up")
     GPIO.cleanup()

def LCDScreen():
     print(Input)
     lcd.text(str(Input), 1, 'center')