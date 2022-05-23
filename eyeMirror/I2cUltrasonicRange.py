from smbus2 import SMBus
import time


class I2cUltrasonicRange:
    def __init__(self):
        self.i2c = SMBus(1)
        # self.i2c.open(1)
        self.i2c_addr = 0x0b

    def detectCM(self):
        self.i2c.open(1)
        range1 = [0, 0, 0]
        for i in range(0, 3):
            try:
                self.i2c.write_byte(self.i2c_addr, 1, force=None)
                time.sleep(0.003)
                b = self.i2c.read_i2c_block_data(self.i2c_addr, 1, 2)
            except:
                print(1)
                b = [340.1,340.1]
            range1[i] = (b[0] + b[1] * 256) / 10
        final_range = ((range1[0] + range1[1] + range1[2]) / 3)
        self.i2c.close()
        if final_range > 340:
            return(-1)
        else:
            print(final_range)
            return (final_range)

a = I2cUltrasonicRange()
print(a.detectCM())