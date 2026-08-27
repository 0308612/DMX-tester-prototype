import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Row_pins = [9, 22, 27, 17]
Col_pins = [16, 5, 6, 26]

key_matrix = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

for row in Row_pins:
     GPIO.setup(row, GPIO.OUT)
     GPIO.output(row, GPIO.LOW)

for col in Col_pins:
     GPIO.setup(col, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("keyboard scanner ready")

try:
     while True:
          for r_idx, Row_pins in enumerate(Row_pins):
                GPIO.output(Row_pins, GPIO.HIGH)
                for c_idx, Col_pins in enumerate(Col_pins):
                    if GPIO.input(Col_pins) == GPIO.HIGH:
                        print(f"key pressed: {key_matrix[r_idx][c_idx]}")
                        while GPIO.input(Col_pins) == GPIO.HIGH:
                            time.sleep(0.05)
                GPIO.output(Row_pins, GPIO.LOW)
                time.sleep(0.02)  

except KeyboardInterrupt:
     print("\ncleaning up")
     GPIO.cleanup()