#串口通信
import serial
import numpy as np
#新建静态类

class Distance:
    #新建静态方法
    @staticmethod
    def get_distance(port):
          #设置串口'/dev/ttyUSB0'
        ser = serial.Serial(port, 115200)
        #串口发送16进制的0x55 0x55 0x00 0x00 0x00 0x00 0x00 0x00 0x00
        hexStr = "5A040400"
        # convert hex to bytes
        bytes_hex = bytes.fromhex(hexStr)

        #新数组
        distances = []
        #循环3次求median值
        for i in range(5):
          #清除串口缓存
          ser.flushInput()
          ser.flushOutput()
          ser.write(bytes_hex)
          #串口接收byte
          data = ser.read(9)
          #取第3和第4个字节转换成十六进制
          #data_hex = data[2:4].hex()
          amp = data[4]  + (data[5]* 256)
          if(amp != 65535 and amp > 100):
              distances.append(data[2]  + (data[3]* 256))         
         
          # print(distances)
        #转换为16进制
        #data_hex = data.hex()
        # print(distances)1·
        #关闭串口
        ser.close()
        return int(np.median(distances)+5)
      
print(Distance.get_distance('/dev/ttyUSB0'))
