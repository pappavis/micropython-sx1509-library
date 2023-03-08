Micropython driver for SX1509 16-channel GPIO with LED Driver and Keypad Engine. This library is work-in-progress.

# IMPORTANT!!
This lib is experimental, may not work. Its my first attempt at an I2C library in Micropython.<br>
Comments/updates here --> <a href="https://forum.micropython.org/viewtopic.php?f=2&t=9178" target="_blank">micropython.org/viewtopic.php?f=2&t=9178</a>.
<br>
<img src="https://cdn.sparkfun.com/r/500-500/assets/parts/1/0/9/5/6/13601-01.jpg" width="10%" hieght="10%">
<br><br>
# NOTE!!
 * PWM & Keypad engine not working yet.
 * Only pins 8 to 15 working as digital expander pins much like a PCF8574.

# Change log:
- 0.0.1 20201021 First release. It can reset, can read & write a value to pin 0.
- 0.0.2 20201029
- 0.0.3 20230301 Bijgewerkt met ChatGPT  https://chat.openai.com
  * Functional working: <i>digitalWrite(pinNr, True|False)</i> works.

# Lijst van TODO
  * TODO: test PWM / LED breaething.
  * TODO: Implementeer het Keypad engine.

# HOWTO: Overzetten naar Micropython
 Stap 1. Download <a href="http://thonny.org">Thonny IDE</a>. <br>
 Stap 2. Verbind aan jouw Micropython apparaat via USB.<br>
 Stap 3. Upload die lib middels Thonny' Save As.. feature.<br>
 Stap 4. Verbind jouw sx1509 aan de ESP32<br>
 Stap 5. Run de democode hieronder in Thonny.<br>

# Rrequirements
 - ESP32 want die lib past niet in een ESP8266.

## Voorbeeld gebruik
WORK-in-Progress!!

```python
import utime
import random
from machine import Pin, PWM, ADC
import esp
import gc
esp.osdebug(None)

gc.collect()

class mainAPP:
    def __init__(self):
        self._adc_pin = 13
        self._adc = (Pin(self._adc_pin))
        random.seed(1024)        

    def main(self):
        aantalLoops =  1000/60 * 60 * 60 * 24
        
        
        led = PWM(Pin(self._adc_pin))
        led.freq(500)
        
        for i1 in range(0, aantalLoops):
            duty1 = int(random.random()*1000)
            for dutCnt1 in range(1, int(random.random()*100)):
                led.duty(duty1)
                utime.sleep_ms(int(random.random()*100))
            
            led.duty(0)
            sleepTime1 = int(random.random()*1000)
            print(f'sleepTime1: {sleepTime1}ms')
            utime.sleep_ms(sleepTime1)
            if(i1 % 10 == 0):
                print("Led knipperen op PIN=",self._adc_pin ,  i1,"van",aantalLoops)
   
   
if __name__ == '__main__':
    print("App start")
    main1 = mainAPP()
    main1.main()
    print("App eind")
```

# Info
- Original <a href="https://learn.sparkfun.com/tutorials/sx1509-io-expander-breakout-hookup-guide">Sparkfun</a> SX1509 lib.
- <a href="https://datasheet.octopart.com/SX1509BIULTRT-Semtech-datasheet-12516845.pdf">Datasheet</a> SX1509


# CREDITS
- Micropython lib michiel@easylab4kids.nl

#easylab4kids
