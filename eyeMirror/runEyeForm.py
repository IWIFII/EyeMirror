from decimal import Decimal
from PySide2.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PySide2.QtCore import Qt, QRect, QRectF
from PySide2.QtGui import QPixmap, QMatrix, QPainter, QFont, QFontDatabase, QFontMetrics, QTextOption
from math import *
import time
import random
import _thread


class eyeWindow(QWidget):
    def __init__(self, fResizedFont, fDistanceFactor):
        nIndex = QFontDatabase.addApplicationFont('Sloan.otf')
        self.sloan = QFontDatabase.applicationFontFamilies(nIndex)[0]
        QWidget.__init__(self)
        self.eyeStatus = ''
        # setGeometry(x_pos, y_pos, width, height)
        # upper left corner coordinates (x_pos, y_pos)
        self.setGeometry(0, 0, 1024, 600)
        self.setWindowTitle('Testing text rotation ...')
        self.setStyleSheet('''
        background-color:black;
        ''')
        self.text = "E"

        self.degrees = 0
        self.resizedFont = fResizedFont
        self.distanceFactor = 5 / fDistanceFactor
        conversion = float(fResizedFont)
        self.currLevel = 5.0
        # print(resizedFont)
        self.factor = 72.72 / conversion
        # 7 inch raspberry 1024*600 dot pitch 0.0642(W) x 0.1790(H)mm
        self.pixerLengthFactorWidth = 1024 / 1920 / 0.0642
        self.pixerLengthFactorHeight = 600 / 1080 / 0.1790
        self.size = round(220 * self.factor / self.distanceFactor)
        # self.window = QMainWindow()
        # self.window.resize(1024, 600)
        # self.window.setWindowTitle('Eye test')
        # self.window.setStyleSheet('''
        # background-color:black;
        # ''')
        # self.label_eye=QLabel(self)
        # self.label_eye.setText('E')
        # self.label_eye.resize(1024, 600)#the 20/20 size for 100 feet #real size is 1.7452756
        # self.label_eye.setStyleSheet('''
        # position:absolute;
        # color: #ffffff;
        # text-align:center;
        # left:0;
        # top:0;
        # bottom:0;
        # right:0;
        # margin:auto;
        # font-size: 126pt;
        # transform: rotate(-90deg);
        # ''')
        # self.label_eye.setAlignment(Qt.AlignCenter)

    def changeSetting(self,fResizedFont,fDistanceFactor):
        self.text = "E"
        self.degrees = 0
        self.resizedFont = fResizedFont
        self.distanceFactor = 5 / fDistanceFactor
        conversion = float(fResizedFont)
        self.currLevel = 5.0
        # print(resizedFont)
        self.factor = 72.72 / conversion
        # 7 inch raspberry 1024*600 dot pitch 0.0642(W) x 0.1790(H)mm
        self.pixerLengthFactorWidth = 1024 / 1920 / 0.0642
        self.pixerLengthFactorHeight = 600 / 1080 / 0.1790
        self.size = round(220 * self.factor / self.distanceFactor)

    def addEyeStatus(self):
        self.eyeStatus += " " + str(self.getVisionAcuity()) + " "

    def getEyeStatus(self):
        return self.eyeStatus

    def addLevel(self):
        self.currLevel = float(Decimal(str(self.currLevel)) + Decimal('0.1'))
        if self.currLevel > 5.3:
            self.currLevel = 5.3
        self.changeLetter(self.currLevel)

    def minusLevel(self):
        self.currLevel = float(Decimal(str(self.currLevel)) - Decimal('0.1'))
        print('minusLevel',type(self.currLevel))
        if self.currLevel < 4.0:
            self.currLevel = 4.0
        self.changeLetter(self.currLevel)

    def randomLetter(self):
        self.changeLetter(self.currLevel)
        
    def getVisionAcuity(self):
        print(self.currLevel)
        return self.currLevel

    def changeBaseLetter(self):
        self.degrees = 0
        self.size = 220

    def changeLetter(self, level, degrees=-1, text='E'):
        self.currLevel = round(level,1)
        deg = [0, 90, 180, 270]
        index = random.randint(0, 3)
        if degrees == -1:
            self.degrees = deg[index]
        else:
            self.degrees = degrees
        self.text = text
        print('lvl:',level)
        # self.degrees=270
        if level == 4.0:  # 20/200
            size = round(220 * (pow(10, 1) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.1:  # 20/100
            size = round(220 * (pow(10, 0.9) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.2:  # 20/80
            size = round(220 * (pow(10, 0.8) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.3:  # 20/70
            size = round(220 * (pow(10, 0.7) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.4:  # 20/60
            size = round(220 * (pow(10, 0.6) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.5:  # 20/50
            size = round(220 * (pow(10, 0.5) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.6:  # 20/40
            size = round(220 * (pow(10, 0.4) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.7:  # 20/30
            size = round(220 * (pow(10, 0.3) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.8:  # 20/25
            size = round(220 * (pow(10, 0.2) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 4.9:  # 20/20
            print('20/20')
            size = round(220 * (pow(10, 0.1) / pow(10, 1)) * self.factor / self.distanceFactor)
            print(size)
        elif level == 5.0:  # 20/15
            size = round(220 * (pow(10, 0) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 5.1:  # 20/15
            size = round(220 * (pow(10, -0.1) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 5.2:  # 20/15
            size = round(220 * (pow(10, -0.2) / pow(10, 1)) * self.factor / self.distanceFactor)
        elif level == 5.3:  # 20/15
            size = round(220 * (pow(10, -0.3) / pow(10, 1)) * self.factor / self.distanceFactor)
        print('size:',size)
        self.size = size
        # self.label_eye.setStyleSheet('''
        # position:absolute;
        # color: #ffffff;
        # text-align:center;
        # left:0;
        # top:0;
        # bottom:0;
        # right:0;
        # margin:auto;
        # font-size: '''+str(size)+'''pt;
        # ''')
        # self.label_eye.setStyleSheet('font-size: '+str(size)+'pt;')
        # self.label_eye.setText('<html><head><style>.box {width: 1024px; height: 30px; transform: rotate(90deg);-ms-transform: rotate(90deg);-moz-transform: rotate(90deg);-webkit-transform: rotate(90deg);-o-transform: rotate(90deg);}</style></head><body><div class="box">E</div></body></html>')
        # self.label_eye.setAlignment(Qt.AlignCenter)

    def paintEvent(self, event):
        '''
            the method paintEvent() is called automatically
            the QPainter class does the low-level painting
            between its methods begin() and end()
            '''
        print('paint')
        qp = QPainter()
        qp.begin(self)
        # set text color, default is black
        qp.setPen('white')
        # QFont(family, size)
        qp.setFont(QFont(self.sloan, self.size))
        # start text at point (x, y)
        # 7 inch raspberry 1024*600 dot pitch 0.0642(W) x 0.1790(H)mm
        x = 1024 / 2
        y = 600 / 2
        # elengthw=self.pixerLengthFactorWidth * self.size*72.72/440
        # elengthh = self.pixerLengthFactorHeight * self.size * 72.72 / 440
        # elengthw=self.size /72 *48
        DPI = 96  # pi=170
        elength = self.size * (1 / 72) * DPI
        print(elength)
        if self.degrees == 0:
            qp.translate(1024 / 2 - elength / 2, 600 / 2 + elength / 2)
        elif self.degrees == 90:
            qp.translate(1024 / 2 - elength / 2, 600 / 2 - elength / 2)
        elif self.degrees == 180:
            qp.translate(1024 / 2 + elength / 2, 600 / 2 - elength / 2)
        elif self.degrees == 270:
            qp.translate(1024 / 2 + elength / 2, 600 / 2 + elength / 2)
        qp.rotate(self.degrees)
        # self_rect = QRectF(0,0,1024,600)
        # self_rect.moveTo(0, 0)
        # textoption=QTextOption(Qt.AlignCenter)
        # qp.drawText(self_rect,self.text,textoption)
        # qp.drawText(self_rect, Qt.AlignLeft, self.text)
        qp.drawText(0, 0, self.text)
        qp.end()


def demoEye(eyeW):
    # eyeW = eyeWindow(2.9,2.5)

    eyeW.changeLetter(5.0, 0)
    eyeW.repaint()
    time.sleep(3)
    eyeW.changeLetter(4.9, 180)
    eyeW.repaint()
    time.sleep(3)

    eyeW.changeLetter(4.8, 90)
    eyeW.repaint()
    time.sleep(3)
    eyeW.changeLetter(4.9, 270)
    eyeW.repaint()
    time.sleep(3)

    eyeW.changeLetter(4.8, 0)
    eyeW.repaint()
    time.sleep(3)
    eyeW.changeLetter(4.9, 180)
    eyeW.repaint()
    time.sleep(3)
    print(eyeW.getVisionAcuity())
    # eyeW.close()
# app.exec_()

# app = QApplication([])
# eyeW = eyeWindow(44.5,2.5)#71#pi44.5
# eyeW.changeLetter(5.0)
# # eyeW.changeBaseLetter()
# #eyeW.show()
# eyeW.showFullScreen()
# #eyeW.window.show()
# #eyeW.window.showFullScreen()
# print(eyeW.getVisionAcuity())
# try:
#     #_thread.start_new_thread(testEye,())
#     #_thread.start_new_thread(updateWeather, (mainw,))
#     pass
# except:
#     print("false")
# app.exec_()
