import RPi.GPIO as GPIO
import time
from rpi_lcd import LCD

# Initialize LCD
lcd = LCD(0x3f, 1, 16, 2, True)

# Setup GPIO
GPIO.setmode(GPIO.BCM)
Col_pins = [9, 22, 27, 17]
Row_pins = [16, 5, 6, 26]

# Map your layout strictly to match rows and columns
# Matrix: [Col 0, Col 1, Col 2, Col 3] for each Row
keypad_map = [
    ["1", "4", "7", "*"],  # Row 0
    ["2", "5", "8", "0"],  # Row 1
    ["3", "6", "9", "#"],  # Row 2
    ["A", "B", "C", "D"]   # Row 3
]

Input = ""

# Configure Rows as Inputs with Pull-Down resistors
for row in Row_pins:
    GPIO.setup(row, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Configure Columns as Outputs, set to LOW initially
for col in Col_pins:
    GPIO.setup(col, GPIO.OUT)
    GPIO.output(col, GPIO.LOW)

def update_lcd():
    """Prints the current string to the LCD."""
    print(f"Current Input: {Input}")
    lcd.clear()
    lcd.text(Input, 1, 'center')

def scan_keypad():
    """Scans the matrix to find which exact key was pressed."""
    global Input
    
    for col_idx, col in enumerate(Col_pins):
        # Set one column HIGH at a time
        GPIO.output(col, GPIO.HIGH)
        
        for row_idx, row in enumerate(Row_pins):
            if GPIO.input(row) == GPIO.HIGH:
                key = keypad_map[row_idx][col_idx]
                
                # Handle special keys
                if key == '#':      # Action key (Enter)
                    print("Entered!")
                    Input = ""
                elif key == '*':    # Reset key
                    print("Input reset!")
                    Input = ""
                else:               # Regular character tracking
                    Input += key
                
                update_lcd()
                
                # Debounce: Wait until the key is released before moving on
                while GPIO.input(row) == GPIO.HIGH:
                    time.sleep(0.05)
                
                GPIO.output(col, GPIO.LOW)
                return
                
        GPIO.output(col, GPIO.LOW)

try:
    print("Keypad ready. Press keys...")
    while True:
        # Keep columns HIGH so any button press pulls a row HIGH
        for col in Col_pins:
            GPIO.output(col, GPIO.HIGH)
            
        # Poll rows for a press
        pressed = False
        for row in Row_pins:
            if GPIO.input(row) == GPIO.HIGH:
                pressed = True
                break
                
        if pressed:
            # Drop all columns back down to prepare for a clean column-by-column scan
            for col in Col_pins:
                GPIO.output(col, GPIO.LOW)
            scan_keypad()
            
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nCleaning up GPIO...")
    GPIO.cleanup()