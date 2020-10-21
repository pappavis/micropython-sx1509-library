# micropython-sx1509-library
Micropython driver for SX1509 16-channel GPIO with LED Driver and Keypad Engine

<img src="https://cdn.sparkfun.com/r/500-500/assets/parts/1/0/9/5/6/13601-01.jpg" width="10%" hieght="10%">

Very early version.

Current status:
- 0.0.1 20201021 It can reset, can read & write a value to pin 0. Thats it!

## Voorbeeld gebruik
WORK-in-Progress!!

```python
import sx1509
wemosPinsDict8266 = {"TX":1, "RX":3,"D4":2, "D3":0, "D2":4, "D1":5, "RX":3, "TX":1, "D8":15, "D7":13, "D6":12, "D5":14, "D0":16, "SCL":5, "SDA":4}
wemosSPI8266 = {"MISO":wemosPinsDict8266["D6"], "MOSI":wemosPinsDict8266["D7"], "SCK":wemosPinsDict8266["D5"], "CSN":wemosPinsDict8266["D4"], "CE":wemosPinsDict8266["D3"]}

sx1 = sx1509(i2c=i2c1, address=i2cAddr)
sx1.reset()
val1 = sx1._read(address=sx1.defs.REG_I_ON_0)
print("1 val1=",val1)


```

# CREDITS
- Micropython lib michiel@easylab4kids.nl
- <a href="https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide">Sparkfun</a> SX1509 lib

