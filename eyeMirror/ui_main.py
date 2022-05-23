# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Main_UI(object):
    def setupUi(self, Main_UI):
        if not Main_UI.objectName():
            Main_UI.setObjectName(u"Main_UI")
        Main_UI.setEnabled(True)
        Main_UI.resize(1024, 600)
        Main_UI.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.label_time = QLabel(Main_UI)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setGeometry(QRect(760, 20, 251, 121))
        font = QFont()
        font.setFamily(u"Snellen 10")
        self.label_time.setFont(font)
        self.label_hitokoto = QLabel(Main_UI)
        self.label_hitokoto.setObjectName(u"label_hitokoto")
        self.label_hitokoto.setGeometry(QRect(-10, 260, 1011, 100))
        self.label_todo = QLabel(Main_UI)
        self.label_todo.setObjectName(u"label_todo")
        self.label_todo.setGeometry(QRect(30, 350, 760, 181))
        self.label_lastvision = QLabel(Main_UI)
        self.label_lastvision.setObjectName(u"label_lastvision")
        self.label_lastvision.setGeometry(QRect(800, 350, 200, 181))
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        self.label_todo.setFont(font1)
        self.label_weather = QLabel(Main_UI)
        self.label_weather.setObjectName(u"label_weather")
        self.label_weather.setGeometry(QRect(20, 30, 461, 181))
        self.label_weather.setFont(font1)

        self.retranslateUi(Main_UI)

        QMetaObject.connectSlotsByName(Main_UI)
    # setupUi

    def retranslateUi(self, Main_UI):
        Main_UI.setWindowTitle(QCoreApplication.translate("Main_UI", u"Main_UI", None))
        self.label_time.setText(QCoreApplication.translate("Main_UI", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">11:45:14</span></p></body></html>", None))
        self.label_hitokoto.setText(QCoreApplication.translate("Main_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-family:'Helvetica Neue','Helvetica','PingFang SC','Hiragino Sans GB','Microsoft YaHei','\u5fae\u8f6f\u96c5\u9ed1','Arial','sans-serif'; font-size:30px; font-weight:600; color:#ffffff;\">\u300e </span><span style=\" font-size:28pt; font-weight:600; color:#ffffff;\">\u70b9\u4eae\u773c\u7738\uff0c\u955c\u5316\u5fc3\u7075</span><span style=\" font-family:'Helvetica Neue','Helvetica','PingFang SC','Hiragino Sans GB','Microsoft YaHei','\u5fae\u8f6f\u96c5\u9ed1','Arial','sans-serif'; font-size:30px; font-weight:600; color:#ffffff;\">\u300f</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">1111111111111111111111111111111111111111</span><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">\u2014\u2014\u7738\u955c</span></p></body></html>", None))
        self.label_todo.setText(QCoreApplication.translate("Main_UI", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">\u5f85\u529e\uff1a</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">1.\u7761\u89c9</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">2.\u6478\u9c7c</span></p></body></html>", None))

        self.label_lastvision.setText(QCoreApplication.translate("Main_UI",
                                                       u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:600; color:#ffffff;\">last vision</span></p><p><span style=\" font-size:16pt; color:#ffffff;\">none</span></p><p><span style=\" font-size:16pt; color:#ffffff;\"></span></p></body></html>",
                                                       None))
        self.label_weather.setText(QCoreApplication.translate("Main_UI", u"<html><head/><body><p><span style=\" font-size:36pt; font-weight:600; color:#ffffff;\">28\u00b0</span><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\"/><span style=\" font-size:18pt; color:#ffffff;\">\u6674 \u897f\u5357\u98ce 2\u7ea7</span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u6e7f\u5ea657.0\uff05 \u7d2b\u5916\u7ebf\u5f3a </span></p><p><span style=\" font-size:18pt; color:#ffffff;\">\u65e5\u51fa06:34 \u65e5\u843d18:32</span></p><p><br/></p></body></html>", None))
    # retranslateUi

