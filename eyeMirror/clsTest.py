#测试视力
from numpy import eye
from clsDistance import Distance
from clsVoice import Voice
import time
from pydub import AudioSegment
from pydub.playback import play

class TestVision:
    def __init__(self,eyeW1,voiceReader):
        self.distance = Distance()
        self.eyeW = eyeW1
        self.voiceReader = voiceReader

    def get_distance(self):
        return self.distance.get_distance('/dev/ttyUSB0')

    def distance_appropriate(self):
        distance = self.get_distance()
        print(distance)
        if distance < 50:
            return 0
        elif distance > 500:
            return 1
        else:
            return 2 
          
    def readVoice(self):
        #10秒后退出      
        d = {0 : 'right' , 90 : 'down' , 180 : 'left' , 270 : 'up'}  
        ans=  self.voiceReader.read()
        i=0      
        while not (ans == 'right' or ans == 'down' or ans == 'left' or ans == 'up'):
            ans=  self.voiceReader.read()
            i+=1
            if i == 10:
                break
            time.sleep(1)
        print(ans,i,d[self.eyeW.degrees])
        return ans == d[self.eyeW.degrees]

    def test3Times(self):
        print('test2Times')
        # d = {0 : 'right' , 90 : 'down' , 180 : 'left' , 270 : 'up'}
        for i in range(0,2):
            self.eyeW.randomLetter()
            self.eyeW.repaint()
            if not self.readVoice():
                return False
        return True

    def test_vision(self):
        #厘米转米
        print("test_vision")
        self.eyeW.showFullScreen()
        distanceM = float(self.get_distance()/100)
        self.eyeW.showFullScreen()
        self.eyeW.changeLetter(4.5, 0, str(distanceM)+'m')
        self.eyeW.repaint()
        while self.distance_appropriate() != 2:
            approp = self.distance_appropriate()
            print(approp)
            if approp == 0:
                distanceM = float(self.get_distance()/100)
                self.eyeW.changeLetter(4.5, 0, str(distanceM)+'m')
                self.eyeW.repaint()  #提示距离过近
                self.voiceReader.write('A3')
                time.sleep(1)

            elif approp == 1:
                distanceM = float(self.get_distance()/100)
                self.eyeW.changeLetter(4.5, 0, str(distanceM)+'m')
                self.eyeW.repaint() #提示距离过远
                self.voiceReader.write('A4')
                time.sleep(1)
        distanceM = float(self.get_distance()/100)
        self.eyeW.changeLetter(4.5, 0, str(distanceM)+'m')
        self.eyeW.repaint()
        time.sleep(0.5)
        self.eyeW.changeSetting(44.5,distanceM)
        time.sleep(0.5)
        self.eyeW.changeLetter(4.5)
        self.eyeW.repaint()
        d = {0 : 'right' , 90 : 'down' , 180 : 'left' , 270 : 'up'}
        slowtest = False
        overZero = False
        print('start')
        while True:
            if slowtest:
                if overZero:
                    if self.test3Times():
                        break
                    else:
                        self.eyeW.minusLevel()
                        overZero = False
                else:
                    if not self.test3Times():
                        self.eyeW.minusLevel()
                        overZero = True
                    else:
                        self.eyeW.addLevel()
                        overZero = False

            elif self.readVoice():
                self.eyeW.addLevel()
            else:
                if not self.test3Times():
                    self.eyeW.minusLevel()
                    slowtest = True
                    overZero = True
            self.eyeW.repaint()
        self.eyeW.changeLetter(4.5, 0, str('T'))
        self.eyeW.repaint()
        return self.eyeW.getVisionAcuity()
        # print('end',self.eyeW.getVisionAcuity())
        # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
        # play(song)
"""         while ans != d[self.eyeW.degrees]:
            ans = a.read()
            print(ans)
            print(d[self.eyeW.degrees],len(d[self.eyeW.degrees])) """

