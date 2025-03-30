# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '������.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Eye_UI(object):
    def setupUi(self, Eye_UI):
        if not Eye_UI.objectName():
            Eye_UI.setObjectName(u"Eye_UI")
        Eye_UI.resize(1024, 600)
        Eye_UI.setStyleSheet(u"\n"
"background-color: rgb(0, 0, 0);")
        self.label_eye = QLabel(Eye_UI)
        self.label_eye.setObjectName(u"label_eye")
        self.label_eye.setGeometry(QRect(-10, -240, 1041, 841))
        font = QFont()
        font.setFamily(u"Sloan.otf")
        self.label_eye.setFont(font)
        self.label_eye.setMargin(0)
        self.retranslateUi(Eye_UI)

        QMetaObject.connectSlotsByName(Eye_UI)
    # setupUi

    def retranslateUi(self, Eye_UI):
        Eye_UI.setWindowTitle(QCoreApplication.translate("Eye_UI", u"Form", None))
        self.label_eye.setText(QCoreApplication.translate("Eye_UI", u"<html><head/><body><p align=\"center\"><span style=\" font-size:600pt; font-weight:0; color:#ffffff;\">E</span></p></body></html>", None))
    # retranslateUi

