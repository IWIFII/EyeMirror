import time
import serial
import _thread

#新建voice类
class Voice:
    #新建初始化函数
    content=""
    def __init__(self, port,timeout=1):
        self.ser = serial.Serial(port, 9600,timeout=timeout)
    
    def read(self):
            data = self.bytes2str(self.ser.readline())
            data = data.replace("\r\n","")
            self.content = data
            return data
    # def read(self):
    #     _thread.start_new_thread(self.readThread,())
    # #新建一个名为read的线程
    # def readThread(self):
    #     while 1:
    #         data = self.bytes2str(self.ser.readline())
    #         data = data.replace("\r\n","")
    #         self.content = data

    def write(self, data):
        data = bytes.fromhex(data)
        return self.ser.write(data)

    def close(self):
        self.ser.close()

    def bytes2str(self,data):
        return data.decode('utf-8')
    

# a = Voice('/dev/ttyUSB1')

# while 1:
#     a.read()
#     print(a.content)
#     time.sleep(1)

#串口发送字符串
# b = 'AA'
# d=bytes.fromhex(b)
# a.write(d)

