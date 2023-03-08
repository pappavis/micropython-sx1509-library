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
