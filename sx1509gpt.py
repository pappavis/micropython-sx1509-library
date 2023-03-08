from machine import I2C
import time
#20230302 Micropython gemaakt met ChatGPT.

class SX1509_LEDDriver:
    # SX1509 LED driver class
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address
        
        # Configure the LED driver settings
        self.i2c.writeto_mem(self.address, 0x1E, b'\x40') # Configuration register: 0x40 = LED driver
        self.i2c.writeto_mem(self.address, 0x20, b'\xFF') # Data direction register: 0xFF = all outputs
        self.i2c.writeto_mem(self.address, 0x21, b'\x00') # Pull-up register: 0x00 = all disabled
        
    def set_pwm(self, pin, value):
        # Set PWM duty cycle for the specified pin (0-255)
        if value < 0:
            value = 0
        elif value > 255:
            value = 255
        self.i2c.writeto_mem(self.address, 0x12 + pin, bytes([value]))
        
    def blink(self, pin, on_time, off_time):
        # Blink the specified pin on and off
        self.i2c.writeto_mem(self.address, 0x11, bytes([1 << pin])) # Enable blink for pin
        self.i2c.writeto_mem(self.address, 0x13 + (2 * pin), bytes([on_time])) # On time
        self.i2c.writeto_mem(self.address, 0x14 + (2 * pin), bytes([off_time])) # Off time
        
    def breathe(self, pin, fade_in_time, fade_out_time):
        # Make the specified pin fade in and out
        self.i2c.writeto_mem(self.address, 0x11, bytes([1 << pin])) # Enable blink for pin
        self.i2c.writeto_mem(self.address, 0x1D, bytes([1 << pin])) # Enable PWM for pin
        self.i2c.writeto_mem(self.address, 0x19 + (2 * pin), bytes([fade_in_time])) # Fade in time
        self.i2c.writeto_mem(self.address, 0x1A + (2 * pin), bytes([fade_out_time])) # Fade out time


from machine import I2C

class SX1509_Keypad:
    # Class for reading input from a 4x4 keypad connected to the SX1509 IC
    def __init__(self, i2c, address):
        self.i2c = i2c
        self.address = address
        self.row_pins = [0, 1, 2, 3] # The row pins on the keypad
        self.col_pins = [4, 5, 6, 7] # The column pins on the keypad
        self.keymap = [
            ['1', '2', '3', 'A'],
            ['4', '5', '6', 'B'],
            ['7', '8', '9', 'C'],
            ['*', '0', '#', 'D']
        ] # The keymap for the keypad
        
        # Configure the SX1509 settings for the keypad
        self.i2c.writeto_mem(self.address, 0x1E, b'\x20') # Configuration register: 0x20 = keypad
        self.i2c.writeto_mem(self.address, 0x20, bytes([0b11110000])) # Data direction register: Rows are inputs, Columns are outputs
        self.i2c.writeto_mem(self.address, 0x21, bytes([0b00001111])) # Pull-up register: Rows are pulled up
        
    def scan(self):
        # Scan the keypad for input
        for i, col_pin in enumerate(self.col_pins):
            self.i2c.writeto_mem(self.address, 0x10, bytes([1 << col_pin])) # Set column pin high
            for j, row_pin in enumerate(self.row_pins):
                val = self.i2c.readfrom_mem(self.address, 0x0A + row_pin, 1)[0]
                if not val & (1 << row_pin):
                    return self.keymap[j][i] # Return the pressed key
            self.i2c.writeto_mem(self.address, 0x10, bytes([0])) # Set column pin low
        return None # No key pressed

