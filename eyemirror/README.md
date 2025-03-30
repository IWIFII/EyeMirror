# 眸镜说明 22/5/23
## 主要文件
1. UI.py (**程序主入口**)
2. clsXXX.py (一些类)
3. ui_xxx.py (UI布局文件)
4. *.otf *.ttf (字体文件)
5. runEyeForm.py (视力检测算法)

## 如何运行
打开树莓派终端**不要使用root账户**，输入以下命令：
```
cd /mirror/pycharm_project_365
python UI.py
```

## 部分类介绍
**所有类的使用必须实例化**

### **clsDistance.py**
距离类，调用了TOF测距
方法:get_distance(port)
port为端口号，一般为tts/USB1
```python
def get_distance(port):
        ser = serial.Serial(port, 115200)
        #串口发送16进制的0x55 0x55 0x00 0x00 0x00 0x00 0x00 0x00 0x00
        hexStr = "5A040400"
        # convert hex to bytes
        bytes_hex = bytes.fromhex(hexStr)
```
获取距离：
```py
get_distance(port)
```
返回实际距离+1，请自行判断误差值
```py
return int(np.median(distances)+1)
```
### **clsVoice.py**
语音识别类，集成了对串口的读写功能
```py
class Voice:
    #新建初始化函数
    content=""
    def __init__(self, port,timeout=1):
        self.ser = serial.Serial(port, 9600,timeout=timeout)
```
初始化类时要求填入**语音识别模块的端口号**

```py
    def read(self):
            data = self.bytes2str(self.ser.readline())
            data = data.replace("\r\n","")
            self.content = data
            return data

    def write(self, data):
        data = bytes.fromhex(data)
        return self.ser.write(data)

    def close(self):
        self.ser.close()

    def bytes2str(self,data):
        return data.decode('utf-8')
```
1. read函数
    * 返回读取的内容，自动替换为字符串型，去除回车换行
2. write函数
    * 向串口写入数据，要求16进制
    * 返回写入的数据
3. close函数
    * 关闭串口
4. bytes2str
    * 16进制to str类型，返回str

语音识别另有程序,用的模块

### **clsTest.py**(测试视力类，重要)



