from PySide2 import QtGui
from PySide2 import QtWidgets
from PySide2 import QtCore
import sys


class VerticalLabel(QtWidgets.QLabel):

    def __init__(self, *args):
        QtWidgets.QLabel.__init__(self, *args)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        # calculate the size of the font
        fm = QtGui.QFontMetrics(painter.font())
        xoffset = int(fm.boundingRect(self.text()).width() / 2)
        yoffset = int(fm.boundingRect(self.text()).height() / 2)
        x = int(self.width() / 2) + yoffset
        y = int(self.height() / 2) - xoffset
        # because we rotated the label, x affects the vertical placement, and y affects the horizontal
        painter.drawText(y, x, self.text())
        painter.end()

    def minimumSizeHint(self):
        size = QtWidgets.QLabel.minimumSizeHint(self)
        return QtCore.QSize(size.height(), size.width())

    def sizeHint(self):
        size = QtWidgets.QLabel.sizeHint(self)
        return QtCore.QSize(size.height(), size.width())


class Example(QtWidgets.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        lbl1 = VerticalLabel('ABSOLUTE')
        lbl1.setFont(QtGui.QFont('Arial', 20))
        lbl1.setStyleSheet("QLabel { background-color : black; color : orange; }");
        lbl2 = VerticalLabel('lbl 2')
        lbl3 = VerticalLabel('lbl 3')
        hBoxLayout = QtWidgets.QHBoxLayout()
        hBoxLayout.addWidget(lbl1)
        hBoxLayout.addWidget(lbl2)
        hBoxLayout.addWidget(lbl3)
        self.setLayout(hBoxLayout)
        self.setGeometry(300, 300, 250, 150)
        self.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()