"""
Driver adapted from stm_src files found at: 

Intended to be minimal adaption for basic distance sensing. Calibration applied manually.
"""
ADDRESS_DEFAULT = 0b0101001 # 0x29
RESULT__RANGE_VAL = 0x062
RESULT__INTERRUPT_STATUS_GPIO = 0x04F
SYSRANGE__START = 0x018
SYSTEM__INTERRUPT_CLEAR = 0x015

class VL6180X:
    def __init__(self, i2c, address=ADDRESS_DEFAULT):
        self.__i2c = i2c
        self.__address = address

    def rangeDataReady(self):
        return (self.readReg(RESULT__INTERRUPT_STATUS_GPIO)[0] & 0x04) != 0

    def readRangeNonBlocking(self):
        range = self.readReg(RESULT__RANGE_VAL)
        self.writeReg(SYSTEM__INTERRUPT_CLEAR, 0x01)
        return range

    def readRangeSingle(self):
        self.writeReg(SYSRANGE__START, 0x01)
        return self.readRangeContinuous()

    def readRangeContinuous(self):
        data = self.readReg(RESULT__RANGE_VAL)
        return data

    def writeReg(self, reg, value):
        self.__i2c.writeto_mem(self.__address, reg, bytes([reg >> 8]))
        self.__i2c.writeto_mem(self.__address, reg, bytes([reg >> 0]))
        self.__i2c.writeto_mem(self.__address, reg, bytes([value]))

    def readReg(self, reg):
        self.__i2c.writeto_mem(self.__address, reg, bytes([reg >> 8]))
        self.__i2c.writeto_mem(self.__address, reg, bytes([reg >> 0]))
        return self.__i2c.readfrom_mem(self.__address, reg, 1)

    def getDistance(self):
        data = self.__i2c.readfrom_mem(self.__address, RESULT__RANGE_VAL, 17, addrsize=16)
        return data
