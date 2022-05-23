from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtCore import Qt
from clsVoice import Voice
from ui_main import Ui_Main_UI
import datetime
import _thread
import time
from clsTest import TestVision
from GetHitokoto import GetHitokoto
from clsWeather import Weather
from clsToDoList import toDoList
from runEyeForm import eyeWindow
from clsDistance import Distance
import keyboard
from I2cUltrasonicRange import I2cUltrasonicRange
from pydub import AudioSegment
from pydub.playback import play


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Main_UI()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            _thread.start_new_thread(listenkb, (mainw,))


def updateTime(mainw):
    while 1:
        nowTime = datetime.datetime.now().strftime("%H:%M:%S")
        mainw.ui.label_time.setText(
            '<html><head/><body><p><span style=" font-size:36pt; font-weight:600; color:#ffffff;">' + nowTime + '</span></p></body></html>')
        time.sleep(1)


def update(mainw):
    while 1:
        Text = GetHitokoto.get()
        msg = Text.split(' ', 1)
        mainw.ui.label_hitokoto.setText(
            '<html><head/><body><p align="center"><span style=" font-size:30px; font-weight:600; color:#ffffff;">『 </span><span style=" font-size:28pt; font-weight:600; color:#ffffff;">' +
            msg[
                0] + '</span><span style=" font-size:30px; font-weight:600; color:#ffffff;">』</span></p><p align="center"><span style=" font-size:14pt; font-weight:600; color:#000000;">1111111111111111111111111111111111111111</span><span style=" font-size:14pt; font-weight:600; color:#ffffff;">——' +
            msg[1] + '</span></p></body></html>')
        time.sleep(10)


def updataTodolist(mainw):
    while 1:
        mainw.ui.label_todo.setText(toDoList.getToDoList())
        time.sleep(10)

def updataWeather(mainw):
    while 1:
        wea = Weather()
        mainw.ui.label_weather.setText(wea.displayToUi('深圳'))
        time.sleep(600)

def eventVoice(voiceReader,mainw):
    while 1:
        content = voiceReader.read()
        if content == 'vision_test':
            voiceReader.write('A0')
            time.sleep(5)
            listenkb(mainw)

def startTest(voiceReader):
    voiceReader.write('A5')

        

# 测试用
def listenkb(mainw):
    # playsound('/mirror/pycharm_project_365/start_vision_test.mp3')
    # keyboard.wait('a')
    # dsts = Distance()
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/prepareVisionTest.wav")
    # play(song)
    # distance = dsts.get_distance('/dev/ttyUSB0')
    # eyeW.changeLetter(4.5, 0, str(distance))
    # eyeW.showFullScreen()
    # mainw.hide()
    # time.sleep(1)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/standAway.wav")
    # play(song)
    # time.sleep(3)
    # eyeW.changeLetter(4.5, 0, "2.5m")
    # eyeW.repaint()
    # time.sleep(1)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/readyStartVision.wav")
    # play(song)
    # time.sleep(1)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/startLeftEye.wav")
    # play(song)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/notice.wav")
    # play(song)
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(5.0, 0)
    # eyeW.repaint()
    # # eyeW.showFullScreen()
    # # mainw.hide()
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(4.9, 180)
    # eyeW.repaint()
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(4.8, 90)
    # eyeW.repaint()
    # time.sleep(3)
    # left = eyeW.getVisionAcuity()
    # eyeW.addEyeStatus()
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/startRightEye.wav")
    # play(song)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/notice.wav")
    # play(song)
    # time.sleep(1)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(4.9, 270)
    # eyeW.repaint()
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(4.8, 0)
    # eyeW.repaint()
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/ring.wav")
    # play(song)
    # eyeW.changeLetter(4.9, 180)
    # eyeW.repaint()
    # time.sleep(3)
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/finishedVisionTest.wav")
    # play(song)
    # right = eyeW.getVisionAcuity()
    # eyeW.addEyeStatus()
    # eyeW.changeLetter(4.9, 0, str(eyeW.getEyeStatus()))
    # eyeW.repaint()
    # time.sleep(3)
    voiceReader.write('A5')
    time.sleep(5)
    mainw.hide()
    test = TestVision(eyeW,voiceReader)
    # _thread.start_new_thread(startTest, (voiceReader,))
    left = test.test_vision()
    voiceReader.write('A6')
    time.sleep(5)
    right = test.test_vision()
    voiceReader.write('A2')
    mainw.ui.label_lastvision.setText(
        '<html><head/><body><p><span style=" font-size:16pt; font-weight:600; color:#ffffff;">最新测试:</span></p><p><span style=" font-size:16pt; font-weight:600; color:#ffffff;"><center>左眼: ' + str(
            left) + '</center></span></p><p><span style=" font-size:16pt; font-weight:600; color:#ffffff;"><center>右眼: ' + str(
            right) + '</center></span></p></body></html>')
    mainw.showFullScreen()
    eyeW.hide()


app = QApplication([])
mainw = MainWindow()
eyeW = eyeWindow(44.5, 2.5)

# mainw.show()
mainw.showFullScreen()
try:
    _thread.start_new_thread(updateTime, (mainw,))
    _thread.start_new_thread(update, (mainw,))
    _thread.start_new_thread(updataTodolist, (mainw,))
    _thread.start_new_thread(updataWeather, (mainw,))
    voiceReader = Voice('/dev/ttyUSB1',1)
    _thread.start_new_thread(eventVoice, (voiceReader,mainw,))
    # _thread.start_new_thread(listenkb, (mainw,))
    # song = AudioSegment.from_wav("/mirror/pycharm_project_365/resoures/prepareVisionTest.wav")
    # play(song)
except:
    print("false")

app.exec_()

# 22/5/19 已完成主要代码