import machine
import utime
import ustruct

class sx1590def:
    REG_OPEN_DRAIN_B     = 0x0a    
    REG_DIR_B            = 0x0e    
    REG_INTERRUPT_MASK_A = 0x13
    REG_LED_DRIVER_ENABLE_B = 0x20
    REG_LED_DRIVER_ENABLE_A = 0x21   

    REG_T_ON_0 = 0x29
    REG_I_ON_0 = 0x2a
    REG_OFF_0  = 0x2b
    
    REG_T_ON_15 = 0x64
    REG_I_ON_15 = 0x64
    REG_OFF_15  = 0x66

    INTERNAL_CLOCK_2MHZ = 2

    def __init__(self):
        pass


class sx1509:
    defs = sx1590def()
    
    def __init__(self, i2c, address=0x3e):
        print("sx1509 init")
        self._i2c = i2c
        self._address = address
        if self._i2c.scan().count(address) == 0:
            raise OSError('SX1509 not found at I2C address {:#x}'.format(address))

    def outRegisters(self, i2c):
        self._i2c.start()
        for tel1 in range(0,255):
            data = i2c.readfrom_mem(i2cAddr, tel1 + (4 * index1), 8)
            print(hex(tel1), ustruct.unpack('<HH', data))
            utime.sleep_ms(100)

        self._i2c.stop()


    def _write(self, address, value):
        self._i2c.writeto_mem(self._address, address, bytearray([value]))


    def onOff(self, pin, pwm=0):        
        pass

    def _read(self, address):
        return self._i2c.readfrom_mem(self._address, address, 1)[0]


    def pindir(self, pin, bInOut):
        modeBit = bytes(0);
        
        if ((bInOut == OUTPUT) or (bInOut == ANALOG_OUTPUT)):
            modeBit = 0
        else:
            modeBit = 1

        tempRegDir = readWord(REG_DIR_B)


    def pwm(self, index, on=None, off=None):
        if on is None or off is None:
            data = self.i2c.readfrom_mem(self.address, 0x06 + 4 * index, 4)
            return ustruct.unpack('<HH', data)
        data = ustruct.pack('<HH', on, off)
        self._i2c.writeto_mem(self._address, 0x06 + 4 * index,  data)



    def reset(self):
        self._write(address=0x7D, value=0x0)
        pass


    def writePin(self, pin, bHighLow):
        tempRegDir = self._read(REG_DIR_B);
        print("tempRegDir=", tempRegDir)

        tempPullUp = int(self._read(REG_PULL_UP_B))
        tempPullDown = int(self._read(REG_PULL_DOWN_B))

        if (highLow):    # if HIGH, do pull-up, disable pull-down
            tempPullUp |= (1<<pin);
            tempPullDown &= ~(1<<pin);
            writeWord(REG_PULL_UP_B, tempPullUp);
            writeWord(REG_PULL_DOWN_B, tempPullDown);
        else:    # If LOW do pull-down, disable pull-up
            tempPullDown |= (1<<pin);
            tempPullUp &= ~(1<<pin);
            writeWord(REG_PULL_UP_B, tempPullUp);
            writeWord(REG_PULL_DOWN_B, tempPullDown);


    def digitalWrite(self, pin, bHighLow):
        writePin(pin, bHighLow)


    def readPin(self, pin):
        REG_DIR_B = 0x0E
        tempRegDir = readWord(REG_DIR_B)        
        tempRegData = readWord(REG_DATA_B)

