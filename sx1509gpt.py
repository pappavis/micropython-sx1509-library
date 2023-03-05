from machine import I2C, Pin
import time

class SX1509:
    def __init__(self, i2c, address=0x3E):
        self.i2c = i2c
        self.address = address
        self.reset()
        
    def write_register(self, reg, data):
        self.i2c.writeto_mem(self.address, reg, bytes([data]))
        
    def read_register(self, reg):
        return self.i2c.readfrom_mem(self.address, reg, 1)[0]

    def reset(self):
        self.write_register(0x7D, 0x12)
        time.sleep_ms(10)
        self.write_register(0x7D, 0x34)
        time.sleep_ms(10)
        self.write_register(0x7D, 0x40)
        time.sleep_ms(10)
    
    def set_pin_direction(self, pin, direction):
        mask = 1 << pin
        if direction == "output":
            self.write_register(0x0C, self.read_register(0x0C) & ~mask)
        else:
            self.write_register(0x0C, self.read_register(0x0C) | mask)
        
    def set_pin_pullup(self, pin, pullup):
        mask = 1 << pin
        if pullup:
            self.write_register(0x06, self.read_register(0x06) | mask)
        else:
            self.write_register(0x06, self.read_register(0x06) & ~mask)
            
    def set_pin_pulldown(self, pin, pulldown):
        mask = 1 << pin
        if pulldown:
            self.write_register(0x06, self.read_register(0x06) | mask)
        else:
            self.write_register(0x06, self.read_register(0x06) & ~mask)

    def set_pin_state(self, pin, state):
        mask = 1 << pin
        if state:
            self.write_register(0x10, self.read_register(0x10) | mask)
        else:
            self.write_register(0x10, self.read_register(0x10) & ~mask)
            
    def set_pin_pwm(self, pin, pwm):
        self.write_register(0x12 + pin * 2, pwm & 0xFF)
        self.write_register(0x13 + pin * 2, (pwm >> 8) & 0xFF)

    def set_led_blink(self, pin, time_on, time_off, rise_time, fall_time):
        mask = 1 << pin
        self.write_register(0x08, self.read_register(0x08) | mask)
        self.write_register(0x2D + pin, time_on)
        self.write_register(0x25 + pin, time_off)
        self.write_register(0x1D + pin, rise_time)
        self.write_register(0x21 + pin, fall_time)
    
    def set_keypad(self, rows, cols):
        self.write_register(0x22, rows)
        self.write_register(0x23, cols)
    
    def read_keypad(self):
        data = self.i2c.readfrom_mem(self.address, 0x03, 2)
        return (data[1] << 8) | data[0]
