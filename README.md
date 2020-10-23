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
from pcf8574 import PCF8574
import sx1509

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

    if(i2c1.scan().count(pcfAddr) == 0):
        print("I2C bord NIET gevonden op", pcfAddr)
    else:
        print("PCF8574 gevonden op", pcfAddr)


    pcf1 = PCF8574(i2c=i2c1, address=pcfAddr)
    for tel2 in range(0,10 ):
        print(tel2, "pcf8574 aan/uit")
        utime.sleep_ms(50)
        pcf1.write(2, True)
        pcf1.write(4, True)
        utime.sleep_ms(50)
        pcf1.write(4, False)

    #i2c1.write(b'123')
    #pca1 = PCA9685(i2c=i2c1, addr=i2cAddr)
    #pca1.freq(freq=4000)
    print("Start sx1509")
    sx1 = SX1509(i2c=i2c1, addr=i2cAddr)
    
    for t4 in range(0, 2):
        #val1=sx1._readWord(addr=t4)
        val1=sx1.digitalRead(pin=8)
        print(hex(t4), "val1=",val1)
    
    #sx1._write(addr=sx1.defs.RegLED_DRIVER_ENABLE_A, value=0xfa)
    #print("2 val1=",val1)
    
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

