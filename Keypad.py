import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Row1 = 26
Row2 = 6
Row3 = 5
Row4 = 16

Column1 = 25
Column2 = 23
Column3 = 24
Column4 = 9

GPIO.setup(Row1, GPIO.OUT)
GPIO.setup(Row2, GPIO.OUT)
GPIO.setup(Row3, GPIO.OUT)
GPIO.setup(Row4, GPIO.OUT)

GPIO.setup(Column1, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Column2, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Column3, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(Column4, GPIO.IN , pull_up_down = GPIO.PUD_DOWN)

def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(Column1) == 1):
        print(characters[0])
    if(GPIO.input(Column2) == 2):
            print(characters[1])
    if(GPIO.input(Column3) == 3):
        print(characters[2])
    if(GPIO.input(Column4) == 4):
        print(characters[3])
    GPIO.output(line, GPIO.LOW)

try:
     while True:
        readLine(Row1, ["1","2","3","A"])
        readLine(Row2, ["4","5","6","B"])
        readLine(Row3, ["7","8","9","C"])
        readLine(Row4, ["*","0","#","D"])
except:
     print("\nApp stopped!")