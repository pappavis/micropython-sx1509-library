from machine import I2C, Pin
import time
from sx1509 import SX1509_Keypad
from sx1509 import SX1509_LEDDriver

# Initialize I2C interface and SX1509 IC address
i2c = I2C(scl=Pin(22), sda=Pin(21))
sx1509_address = 0x3E

# Initialize the SX1509 LED driver and the LED it controls
led_driver = SX1509_LEDDriver(i2c, sx1509_address, 1)
led = led_driver.leds[0]

# Initialize the SX1509 keypad
keypad = SX1509_Keypad(i2c, sx1509_address)

while True:
    key = keypad.scan() # Scan for keypad input
    
    if key == 'A':
        # Breathe the LED if the 'A' key is pressed
        led.breathe(1, 255, 0.5, 0.5)

