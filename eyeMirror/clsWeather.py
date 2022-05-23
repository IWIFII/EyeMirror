import requests

#新建一个类 获取当前的天气
class Weather:
    #定义一个类变量
    url = 'http://wthrcdn.etouch.cn/weather_mini?city='

    #定义一个类方法
    def get(self,city):
        #获取天气的url
        url = self.url + city
        data = requests.get(url).json()
        data = data['data']['forecast'][0]
        self.weather = data['type']
        self.high = data['high']
        self.low = data['low']
        self.fengxiang = data['fengxiang']
        self.fengli = data['fengli']
        self.date = data['date']

    def displayToUi(self,i):
        self.get(i)
        #<html><head/><body><p><span style=" font-size:36pt; font-weight:600; color:#ffffff;">28°</span><span style=" font-size:48pt; font-weight:600; color:#ffffff;"/><span style=" font-size:18pt; color:#ffffff;">晴 西南风 2级</span></p><p><span style=" font-size:18pt; color:#ffffff;">湿度57.0％ 紫外线强 </span></p><p><span style=" font-size:18pt; color:#ffffff;">日出06:34 日落18:32</span></p><p><br/></p></body></html>
        html = '<html><head/><body><p><span style=" font-size:36pt; font-weight:600; color:#ffffff;">'+self.getNum(self.high)+'°~'+self.getNum(self.low)+'°</span><span style=" font-size:48pt; font-weight:600; color:#ffffff;"/><br/><span style=" font-size:18pt; color:#ffffff;">'+self.weather+' '+self.fengxiang+' '+self.getNum(self.fengli)+'级 '+'</span></p><span style=" font-size:18pt; color:#ffffff;">'+self.date+'<p><br/></body></html>'
        return html
    

    #取字符串中的数字
    def getNum(self,str):
        num = ''
        for i in str:
            if i.isdigit():
                num += i
        return num

