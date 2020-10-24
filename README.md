# micropython-sx1509-library
Micropython driver for SX1509 16-channel GPIO with LED Driver and Keypad Engine


This library does NOT work, not yet.  Clone the repo, and improve please.


<img src="https://cdn.sparkfun.com/r/500-500/assets/parts/1/0/9/5/6/13601-01.jpg" width="10%" hieght="10%">

Very early version.

Current status:
- 0.0.1 20201021 It can reset, can read & write a value to pin 0. Thats it!

## Voorbeeld gebruik
WORK-in-Progress!!

```python
import machine
import utime
import ustruct

def main():
    global i2cAddr
    global index1
    i2cAddr = int(0x3e)
    pcfAddr = 0x23
    index1 = 1
    
    wemosPinsDict8266 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL":5, "SDA":4}
    wemosSPI8266 = {"MISO":wemosPinsDict8266["D6"], "MOSI":wemosPinsDict8266["D7"], "SCK":wemosPinsDict8266["D5"], "CSN":wemosPinsDict8266["D4"], "CE":wemosPinsDict8266["D3"]}
    
    i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SCL"]),sda=machine.Pin(wemosPinsDict8266["SDA"]),freq=100000)
    
    if(i2c1.scan().count(i2cAddr) == 0):
        print("I2C bord NIET gevonden op", i2cAddr)
    else:
        print("SX1509 gevonden op", i2cAddr)


    SX1509_LED_PIN = 8
    io = SX1509(i2c=i2c1, addr=i2cAddr)
    
    io.pinMode(pin=8, inOut=io.defs.OUTPUT)
    io.pinMode(pin=8, inOut=io.defs.INPUT_PULLUP)
    
    for cnt1 in range(0,5):
        io.digitalWrite(SX1509_LED_PIN, io.defs.HIGH)
        utime.sleep_ms(50)
        io.digitalWrite(SX1509_LED_PIN, io.defs.LOW)
        utime.sleep_ms(10)
    
    print("Eind sx1509")
    
    #Hallo123naarI2C(i2c1=i2c1)

print("APP start")
main()
print("APP eind")

```

# Info
- Original <a href="https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide">Sparkfun</a> SX1509 lib.
- <a href="https://datasheet.octopart.com/SX1509BIULTRT-Semtech-datasheet-12516845.pdf">Datasheet</a> SX1509


# CREDITS
- Micropython lib michiel@easylab4kids.nl

