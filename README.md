# micropython-sx1509-library
Micropython driver for SX1509 16-channel GPIO with LED Driver and Keypad Engine

This library is work-in-progress.

<img src="https://cdn.sparkfun.com/r/500-500/assets/parts/1/0/9/5/6/13601-01.jpg" width="10%" hieght="10%">

Current status:
- 0.0.1 20201021 First release. It can reset, can read & write a value to pin 0.
- 0.0.2 20201029
  * Functional working.
  * Implemented <i>digitalWrite(pin, HIGH|LOW)</i>.  Note: heavily work-in-progress.
  * PWM implemented, not tested.

# Overzetten naar Micropython
 Stap 1. Download <a href="http://thonny.org">Thonny IDE</a>. <br>
 Stap 2. Verbind aan jouw Micropython apparaat via USB.<br>
 Stap 3. Upload die lib middels Thonny' Save As.. feature.<br>
 Stap 4. Verbind jouw sx1509 aan de ESP32<br>
 Stap 5. Run de democode hieronder in Thonny.<br>

## Voorbeeld gebruik
WORK-in-Progress!!

```python
import machine
import utime
import ustruct

def main():
    global i2cAddr
    global index1
    i2cAddr = 0x3e
    pcfAddr = 0x23
    index1 = 1
    i2c1 = None
    
    wemosPinsDict8266 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL":5, "SDA":4}
    wemosSPI8266 = {"MISO":wemosPinsDict8266["D6"], "MOSI":wemosPinsDict8266["D7"], "SCK":wemosPinsDict8266["D5"], "CSN":wemosPinsDict8266["D4"], "CE":wemosPinsDict8266["D3"]}
    
    wemosPinsESP32 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL0":21, "SDA0":22}


    if(sys.platform == 'esp8266'):
        i2c1 = machine.I2C(scl=machine.Pin(wemosPinsDict8266["SCL"]),sda=machine.Pin(wemosPinsDict8266["SDA"]),freq=100000)
    else:
        i2c1 = machine.SoftI2C(scl=machine.Pin(wemosPinsESP32["SCL0"]),sda=machine.Pin(wemosPinsESP32["SDA0"]),freq=100000)


    if(i2c1.scan().count(i2cAddr) == 0):
        print("I2C bord NIET gevonden op", i2cAddr)
    else:
        print("SX1509 gevonden op", i2cAddr)

    io = SX1509(i2c=i2c1, addr=i2cAddr)
    
    print("Setting pins to OUTPUT")
    for pinNr in range(1,16):
        io.pinMode(pinNr, inOut=io.defs.OUTPUT)

    print("Pins aan/uit")
    for ledPin in range(1,16):
        io.digitalWrite(ledPin, io.defs.HIGH)
        utime.sleep_ms(50)
        io.digitalWrite(ledPin, io.defs.LOW)
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

#easylab4kids
