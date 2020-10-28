import machine

class SX1590def:
    RegInputDisableB  = 0x00
    RegInputDisableA  = 0x01
    RegPullUpB        = 0x06
    RegPullUpA        = 0x07
    RegOpenDrainB     = 0x0A 
    RegOpenDrainA     = 0x0B
    RegPolarityB      = 0x0C
    RegPolarityA      = 0x0D
    RegDirB           = 0x0E
    RegDirA           = 0x0F
    RegDataB          = 0x10
    RegDataA          = 0x11
    RegInterruptMaskA = 0x13
    RegClock            = 0x1E
    RegMisc             = 0x1F
    RegLEDDriverEnableB = 0x20
    RegLEDDriverEnableA = 0x21   

    RegReset   = 0x7D
    RegTest1   = 0x7E
    RegTest2   = 0x7F

    INTERNAL_CLOCK_2MHZ = 2
    ANALOG_OUTPUT = 0x3
    OUTPUT = 2
    INPUT_PULLUP = 3
    LedLinear = 0
    LedLogarithmic = 1
    SLAVE_ADDRESS = 0x3E
    HIGH = 255
    LOW  = 0
    pinRESET = -1


    def __init__(self):
        self._REG_T_ON_0 = 0x29    #  RegTOn0 ON time register for I/O[0] 0000 0000
        self._REG_I_ON_0 = 0x2A    #  RegIOn0 ON intensity register for I/O[0] 1111 1111
        self._REG_OFF_0  = 0x2B    #  RegOff0 OFF time/intensity register for I/O[0] 0000 0000
        self._REG_T_ON_1 = 0x2C    #  RegTOn1 ON time register for I/O[1] 0000 0000
        self._REG_I_ON_1 = 0x2D    #  RegIOn1 ON intensity register for I/O[1] 1111 1111
        self._REG_OFF_1  = 0x2E    #  RegOff1 OFF time/intensity register for I/O[1] 0000 0000
        self._REG_T_ON_2 = 0x2F    #  RegTOn2 ON time register for I/O[2] 0000 0000
        self._REG_I_ON_2 = 0x30    #  RegIOn2 ON intensity register for I/O[2] 1111 1111
        self._REG_OFF_2  = 0x31    #  RegOff2 OFF time/intensity register for I/O[2] 0000 0000
        self._REG_T_ON_3 = 0x32    #  RegTOn3 ON time register for I/O[3] 0000 0000
        self._REG_I_ON_3 = 0x33    #  RegIOn3 ON intensity register for I/O[3] 1111 1111
        self._REG_OFF_3  = 0x34    #  RegOff3 OFF time/intensity register for I/O[3] 0000 0000
        self._REG_T_ON_4 = 0x35    #  RegTOn4 ON time register for I/O[4] 0000 0000
        self._REG_I_ON_4 = 0x36    #  RegIOn4 ON intensity register for I/O[4] 1111 1111
        self._REG_OFF_4  = 0x37    #  RegOff4 OFF time/intensity register for I/O[4] 0000 0000
        self._REG_T_RISE_4  = 0x38    #  RegTRise4 Fade in register for I/O[4] 0000 0000
        self._REG_T_FALL_4  = 0x39    #  RegTFall4 Fade out register for I/O[4] 0000 0000
        self._REG_T_ON_5    = 0x3A    #  RegTOn5 ON time register for I/O[5] 0000 0000
        self._REG_I_ON_5    = 0x3B    #  RegIOn5 ON intensity register for I/O[5] 1111 1111
        self._REG_OFF_5     = 0x3C    #  RegOff5 OFF time/intensity register for I/O[5] 0000 0000
        self._REG_T_RISE_5  = 0x3D    #  RegTRise5 Fade in register for I/O[5] 0000 0000
        self._REG_T_FALL_5  = 0x3E    #  RegTFall5 Fade out register for I/O[5] 0000 0000
        self._REG_T_ON_6    = 0x3F    #  RegTOn6 ON time register for I/O[6] 0000 0000
        self._REG_I_ON_6    = 0x40    #  RegIOn6 ON intensity register for I/O[6] 1111 1111
        self._REG_OFF_6     = 0x41    #  RegOff6 OFF time/intensity register for I/O[6] 0000 0000
        self._REG_T_RISE_6  = 0x42    #  RegTRise6 Fade in register for I/O[6] 0000 0000
        self._REG_T_FALL_6  = 0x43    #  RegTFall6 Fade out register for I/O[6] 0000 0000
        self._REG_T_ON_7    = 0x44    #  RegTOn7 ON time register for I/O[7] 0000 0000
        self._REG_I_ON_7    = 0x45    #  RegIOn7 ON intensity register for I/O[7] 1111 1111
        self._REG_OFF_7     = 0x46    #  RegOff7 OFF time/intensity register for I/O[7] 0000 0000
        self._REG_T_RISE_7  = 0x47    #  RegTRise7 Fade in register for I/O[7] 0000 0000
        self._REG_T_FALL_7  = 0x48    #  RegTFall7 Fade out register for I/O[7] 0000 0000
        self._REG_T_ON_8    = 0x49    #  RegTOn8 ON time register for I/O[8] 0000 0000
        self._REG_I_ON_8    = 0x4A    #  RegIOn8 ON intensity register for I/O[8] 1111 1111
        self._REG_OFF_8     = 0x4B    #  RegOff8 OFF time/intensity register for I/O[8] 0000 0000
        self._REG_T_ON_9    = 0x4C    #  RegTOn9 ON time register for I/O[9] 0000 0000
        self._REG_I_ON_9    = 0x4D    #  RegIOn9 ON intensity register for I/O[9] 1111 1111
        self._REG_OFF_9     = 0x4E    #  RegOff9 OFF time/intensity register for I/O[9] 0000 0000
        self._REG_T_ON_10   = 0x4F    #  RegTOn10 ON time register for I/O[10] 0000 0000
        self._REG_I_ON_10   = 0x50    #  RegIOn10 ON intensity register for I/O[10] 1111 1111
        self._REG_OFF_10    = 0x51    #  RegOff10 OFF time/intensity register for I/O[10] 0000 0000
        self._REG_T_ON_11   = 0x52    #  RegTOn11 ON time register for I/O[11] 0000 0000
        self._REG_I_ON_11   = 0x53    #  RegIOn11 ON intensity register for I/O[11] 1111 1111
        self._REG_OFF_11    = 0x54    #  RegOff11 OFF time/intensity register for I/O[11] 0000 0000
        self._REG_T_ON_12   = 0x55    #  RegTOn12 ON time register for I/O[12] 0000 0000
        self._REG_I_ON_12   = 0x56    #  RegIOn12 ON intensity register for I/O[12] 1111 1111
        self._REG_OFF_12    = 0x57    #  RegOff12 OFF time/intensity register for I/O[12] 0000 0000
        self._REG_T_RISE_12 = 0x58    #  RegTRise12 Fade in register for I/O[12] 0000 0000
        self._REG_T_FALL_12 = 0x59    #  RegTFall12 Fade out register for I/O[12] 0000 0000
        self._REG_T_ON_13   = 0x5A    #  RegTOn13 ON time register for I/O[13] 0000 0000
        self._REG_I_ON_13   = 0x5B    #  RegIOn13 ON intensity register for I/O[13] 1111 1111
        self._REG_OFF_13    = 0x5C    #  RegOff13 OFF time/intensity register for I/O[13] 0000 0000
        self._REG_T_RISE_13 = 0x5D    #  RegTRise13 Fade in register for I/O[13] 0000 0000
        self._REG_T_FALL_13 = 0x5E    #  RegTFall13 Fade out register for I/O[13] 0000 0000
        self._REG_T_ON_14   = 0x5F    #  RegTOn14 ON time register for I/O[14] 0000 0000
        self._REG_I_ON_14   = 0x60    #  RegIOn14 ON intensity register for I/O[14] 1111 1111
        self._REG_OFF_14    = 0x61    #  RegOff14 OFF time/intensity register for I/O[14] 0000 0000
        self._REG_T_RISE_14 = 0x62    #  RegTRise14 Fade in register for I/O[14] 0000 0000
        self._REG_T_FALL_14 = 0x63    #  RegTFall14 Fade out register for I/O[14] 0000 0000
        self._REG_T_ON_15   = 0x64    #  RegTOn15 ON time register for I/O[15] 0000 0000
        self._REG_I_ON_15   = 0x65    #  RegIOn15 ON intensity register for I/O[15] 1111 1111
        self._REG_OFF_15    = 0x66    #  RegOff15 OFF time/intensity register for I/O[15] 0000 0000
        self._REG_T_RISE_15 = 0x67    #  RegTRise15 Fade in register for I/O[15] 0000 0000
        self._REG_T_FALL_15 = 0x68    #  RegTFall15 Fade out register for I/O[15] 0000 0000

        self.RegIOn = [self._REG_I_ON_0, self._REG_I_ON_1, self._REG_I_ON_2, self._REG_I_ON_3,
                            self._REG_I_ON_4, self._REG_I_ON_5, self._REG_I_ON_6, self._REG_I_ON_7,
                            self._REG_I_ON_8, self._REG_I_ON_9, self._REG_I_ON_10, self._REG_I_ON_11,
                            self._REG_I_ON_12, self._REG_I_ON_13, self._REG_I_ON_14, self._REG_I_ON_15]

        self.RegTOn = [self._REG_T_ON_0, self._REG_T_ON_1, self._REG_T_ON_2, self._REG_T_ON_3,
                            self._REG_T_ON_4, self._REG_T_ON_5, self._REG_T_ON_6, self._REG_T_ON_7,
                            self._REG_T_ON_8, self._REG_T_ON_9, self._REG_T_ON_10, self._REG_T_ON_11,
                            self._REG_T_ON_12, self._REG_T_ON_13, self._REG_T_ON_14, self._REG_T_ON_15]


        self.RegOff = [self._REG_OFF_0, self._REG_OFF_1, self._REG_OFF_2, self._REG_OFF_3,
                            self._REG_OFF_4, self._REG_OFF_5, self._REG_OFF_6, self._REG_OFF_7,
                            self._REG_OFF_8, self._REG_OFF_9, self._REG_OFF_10, self._REG_OFF_11,
                            self._REG_OFF_12, self._REG_OFF_13, self._REG_OFF_14, self._REG_OFF_15]


        self.RegTRise = [0xFF, 0xFF, 0xFF, 0xFF,
                        self._REG_T_RISE_4, self._REG_T_RISE_5, self._REG_T_RISE_6, self._REG_T_RISE_7,
                        0xFF, 0xFF, 0xFF, 0xFF,
                        self._REG_T_RISE_12, self._REG_T_RISE_13, self._REG_T_RISE_14, self._REG_T_RISE_15]


        self.RegTFall = [0xFF, 0xFF, 0xFF, 0xFF,
                        self._REG_T_FALL_4, self._REG_T_FALL_5, self._REG_T_FALL_6, self._REG_T_FALL_7,
                        0xFF, 0xFF, 0xFF, 0xFF,
                        self._REG_T_FALL_12, self._REG_T_FALL_13, self._REG_T_FALL_14, self._REG_T_FALL_15]


class SX1509:
    defs = SX1590def()
    
    def __init__(self, i2c, addr=0x3e):
        print("sx1509 init")
        self._i2c = i2c
        self._addr = addr
        self._buf1 = bytearray(2)
        if self._i2c.scan().count(addr) == 0:
            raise OSError('SX1509 not found at I2C addr {:#x}'.format(addr))


        tstReg = self._readWord(self.defs.RegInterruptMaskA); # This should return 0xFF00
        if(tstReg == 0xFF00):
            print("SX1509__init success.")


    def _write(self, addr, val):
        self._i2c.writeto_mem(self._addr, addr, int(val).to_bytes(1, "little"))


    def _ledDriverInit(self, pin, freq=1, log=False):
        tempWord = 0
        tempByte = bytes(0)
        
        tempWord = self._readWord(self.defs.RegInputDisableB)[0]
        tempWord |= (1<<pin)
        
        #Disable pull-up
        tempWord = self._readWord(self.defs.RegPullUpB)[0]
        tempWord |= (1<<pin)        
        self._writeWord(addr=self.defs.RegPullUpB, val=tempWord)
        
        # Set direction to output (REG_DIR_B)
        tempWord = self._readWord(self.defs.RegDirB)[0]
        tempWord &= ~(1<<pin); #0=output  
        self._writeWord(addr=self.defs.RegDirB, val=tempWord)

        # Enable oscillator (REG_CLOCK)
        tempByte = self._readByte(self.defs.RegClock)
        tempByte |= (1<<6) # Internal 2MHz oscillator part 1 (set bit 6)
        tempByte &= ~(1<<5)    # Internal 2MHz oscillator part 2 (clear bit 5)
        self._writeByte(self.defs.RegClock, tempByte)


    def _read(self, addr):
        readMem = self._i2c.readfrom_mem_into(self._addr, addr, self._buf1)
        return readMem


    def _pindir(self, pin, inOut):
        modeBit = False;
        
        if ((inOut == self.defs.OUTPUT) or (inOut == self.defs.ANALOG_OUTPUT)):
            modeBit = False
        else:
            modeBit = True

        tempRegDir = self._readWord(addr=self.defs.RegDirB)[0]
        if (modeBit):
            tempRegDir = (1<<pin)
        else:
            tempRegDir &= ~(1<<pin)

        self._writeWord(addr=self.defs.RegDirB, val=tempRegDir)

        # If INPUT_PULLUP was called, set up the pullup too:
        if (inOut == INPUT_PULLUP):
            self._writePin(pin, HIGH)
        
        if (inOut == ANALOG_OUTPUT):
            self._ledDriverInit(pin)


    def pwm(self, pin, iOn):
        '''Write the on intensity of pin
        Linear mode: Ion = iOn
        Log mode: Ion = f(iOn)'''
        self._writeByte(self.defs.RegIOn[pin], iOn)


    def __pwm__nietgebruiken(self, index, on=None, off=None):
        if(on is None or off is None):
            data = self._i2c.readfrom_mem(self.addr, 0x06 + 4 * index, 4)
            return ustruct.unpack('<HH', data)
        data = ustruct.pack('<HH', on, off)
        self._i2c.writeto_mem(self.addr, 0x06 + 4 * index,  int(val).to_bytes(data, "little"))


    def debounceEnable(pin):
        debounceEnable = self._read(addr=defs.RegDebounceEnableB)
        debounceEnable |= (1<<pin)
        self._write(addr=defs.RegDEBOUNCE_ENABLE_B, val=debounceEnable)
        

    def reset(self, hard=True):        
        if(hard):
            regMisc = self._readWord(self.defs.RegMisc)            
            if (regMisc & (1<<2)):
                regMisc &= ~(1<<2)
                self._writeWord(self.defs.RegMisc, regMisc)
            
            rstPin = self.defs.pinRESET
            self.pinMode(rstPin, self.defs.OUTPUT)
            self.digitalWrite(rstPin, self.defs.LOW)
            utime.delay_ms(1)
            self.digitalWrite(rstPin, self.defs.HIGH)
        else:            
            self._writeWord(self.defs.RegReset, 0x12)
            self._writeWord(self.defs.RegReset, 0x34)
        


    def _writePin(self, pin, highLow):
        tempRegDir = self._readWord(addr=self.defs.RegDirB)[0]
        #print("_writePin. tempRegDir=", tempRegDir)

        if ((0xFFFF^tempRegDir)&(1<<pin)): #output mode
            tempRegData = self._readWord(self.defs.RegDataB)[0]

            if (highLow):
                tempRegData |= (1<<pin)
            else:
                tempRegData &= ~(1<<pin)
            
            self._writeWord(self.defs.RegDataB, tempRegData);


    def _writeWord(self, addr, val):
        lsb = bytes(0)
        msb = bytes(0)
        msb = ((int(val) & 0xFF00) >> 8)
        lsb = (int(val) & 0xFF00)
        self._i2c.writeto_mem(self._addr, addr, lsb.to_bytes(1, "little"))
        self._i2c.writeto_mem(self._addr, addr, msb.to_bytes(1, "little"))


    def _writeByte(self, addr, val):
        self._i2c.writeto_mem(self._addr, addr, val.to_bytes(1, "little"))


    def digitalWrite(self, pin, highLow):
        self._writePin(pin, highLow)


    def _pinDir(self, pin, inOut):
        modeBit = bytes(0)

        if ((inOut == self.defs.OUTPUT) or (inOut == self.defs.ANALOG_OUTPUT)):
            modeBit = False
        else:
            modeBit = True
            
        tempRegDir = self._readWord(addr=self.defs.RegDirB)[0]
        if (modeBit):    
            tempRegDir |= (1<<pin)
        else:
            tempRegDir &= ~(1<<pin)
        
        self._writeWord(self.defs.RegDirB, tempRegDir)

        #If INPUT_PULLUP was called, set up the pullup too:
        if (inOut == self.defs.INPUT_PULLUP):
            self._writePin(pin, self.defs.HIGH)

        if (inOut == self.defs.ANALOG_OUTPUT):
            self._ledDriverInit(pin);


    def pinMode(self, pin, inOut):
        self._pinDir(pin, inOut);


    def _readWord(self, addr):
        readValue = 0
        msb = 0
        lsb = 0
        self._i2c.writeto(self._addr, (0).to_bytes(1, "big"))
        rec1 = self._i2c.readfrom_mem(self._addr, addr, 2)
        
        msb = (rec1[0] & 0x00FF) << 8
        lsb = (rec1[1] & 0x00FF)
        readValue = msb , lsb

        return readValue;


    def _readByte(self, addr):
        val = bytes(0)        
        val = self._readWord(addr=addr)[0]
        
        return val


    def _readPin(self, pin):
        tempRegDir = self._readWord(addr=self.defs.RegDirB)[0]
        # print("readPin:", pin ," tempRegDir=", tempRegDir)
        
        if (tempRegDir & (1<<pin)):  # If the pin is an input
            tempRegData = self._readWord(addr=self.defs.RegDataB)[0]
            if (tempRegData & (1<<pin)):
                return 1
    
        return 0


    def digitalRead(self, pin):
        return self._readPin(pin)
    

    def analogWrite(self, pin, iOn):
        self.pwm(pin, iOn)

