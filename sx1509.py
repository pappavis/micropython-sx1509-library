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

    RegTOn0 = 0x29
    RegIOn0 = 0x2a
    RegOff0  = 0x2b

    RegTOn8 = 0x49
    RegIOn8 = 0x4A
    RegOff8 = 0x4B

    RegT_ON_15 = 0x64
    RegI_ON_15 = 0x64
    RegOFF_15  = 0x66
    
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


    def __init__(self):
        pass


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
        self._i2c.writeto_mem(self._addr, addr, bytearray([val]))


    def _ledDriverInit(self, freq=1, log=False):
        self._write(addr=defs.RegInputDisableB, val=bin(pin))
        self._write(addr=defs.RegPULL_UP_B, val=0)
        self._write(addr=defs.RegOPEN_DRAIN_B, val=0)
        self._write(addr=defs.RegDIR_B, val=0b11111111)
        self._write(addr=defs.RegCLOCK, val=0b0)
        self._write(addr=defs.RegLED_DRIVER_ENABLE_B, val=0b11111111)
        self._write(addr=defs.RegT_ON_8, val=0b11111111)
        self._write(addr=defs.RegDATA_B, val=0b11111111)


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


    def pwm(self, index, on=None, off=None):
        if(on is None or off is None):
            data = self._i2c.readfrom_mem(self.addr, 0x06 + 4 * index, 4)
            return ustruct.unpack('<HH', data)
        data = ustruct.pack('<HH', on, off)
        self._i2c.writeto_mem(self.addr, 0x06 + 4 * index,  data)


    def debounceEnable(pin):
        debounceEnable = self._read(addr=defs.RegDebounceEnableB)
        debounceEnable |= (1<<pin)
        self._write(addr=defs.RegDEBOUNCE_ENABLE_B, val=debounceEnable)
        

    def reset(self, hardware):
        regMisc = self._read(self.defs.RegMisc)
        if (regMisc & (1<<2)):
            regMisc &= ~(1<<2)
            self._write(self.defs.RegMisc, regMisc)
        
        self._write(addr=self.defs.RegReset, val=0x12)
        pass


    def _writePin(self, pin, highLow):
        tempRegDir = int(self._readWord(addr=self.defs.RegDirB))
        #print("_writePin. tempRegDir=", tempRegDir)

        if ((0xFFFF^tempRegDir[0])&(1<<pin)): #output mode
            tempRegData = int(self._readword(self.defs.RegDataB))

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
        self._i2c.writeto_mem(self._addr, addr, msb)
        self._i2c.writeto_mem(self._addr, addr, lsb)


    def digitalWrite(self, pin, highLow):
        self._writePin(pin, highLow)


    def _pinDir(pin, inOut):
        modeBit = bytes(0)

        if ((self.defs.inOut == OUTPUT) or (inOut == self.defs.ANALOG_OUTPUT)):
            modeBit = False
        else:
            modeBit = True
            
        tempRegDir = self._read(addr=self.defs.RegDirB)
        #if (modeBit)    
        #    tempRegDir |= (1<<pin);
        #else
        #    tempRegDir &= ~(1<<pin);
        
        self._write(REG_DIR_B, tempRegDir)


    def pinMode(self, pin, inOut):
        self._pinDir(pin, inOut);


    def _readWord(self, addr):
        readValue = None
        msb = 0
        lsb = 0
        self._i2c.writeto(self._addr, (0).to_bytes(0, "big"))
        rec1 = self._i2c.readfrom_mem(self._addr, addr, 2)
        
        msb = (rec1[0] & 0x00FF) << 8
        lsb = (rec1[1] & 0x00FF)
        readValue = msb , lsb

        return readValue;


    def _readByte(self, addr):
        val = bytes(0)
        
        self._i2c.write(addr)
        val = self._i2c.readfrom(addr, 1)
        
        return val


    def _readPin(self, pin):
        tempRegDir = self._readWord(addr=self.defs.RegDirB)[0]
        print("readPin:", pin ," tempRegDir=", tempRegDir)
        retV = None
        
        if (tempRegDir & (1<<pin)):  # If the pin is an input
            tempRegData = self._readWord(addr=self.defs.RegDataB)[0]
            if (tempRegData & (1<<pin)):
                retV = 1
            else:
                retV = 0
    
        return retV


    def digitalRead(self, pin):
        return self._readPin(pin)
    

    def analogWrite(self, pin, iOn):
        self.pwm(pin, iOn)
        
