import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Col_pins = [9, 22, 27, 17]
Row_pins = [16, 5, 6, 26]

for row in Row_pins:
     GPIO.setup(row, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

for col in Col_pins:
     GPIO.setup(col, GPIO.OUT)

def readLine(line, characters):
     GPIO.output(line, GPIO.HIGH)
     if(GPIO.input(Row_pins[0]) == 1):
          print(characters[0])
     if(GPIO.input(Row_pins[1]) == 1):
          print(characters[1])
     if(GPIO.input(Row_pins[2]) == 1):
          print(characters[2])
     if(GPIO.input(Row_pins[3]) == 1):
          print(characters[3])
     GPIO.output(line, GPIO.LOW)

try:
     while True:
          readLine(Col_pins[0], ["1","2","3","A"])
          readLine(Col_pins[1], ["4","5","6","B"])
          readLine(Col_pins[2], ["7","8","9","C"])
          readLine(Col_pins[3], ["*","0","#","D"])
          time.sleep(0.1)
          
except KeyboardInterrupt:
     print("\ncleaning up")
     GPIO.cleanup()

