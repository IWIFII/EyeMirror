from PySide2.QtWidgets import QApplication, QMainWindow
from ui_eye import Ui_Eye_UI


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        # 使用ui文件导入定义界面类
        self.ui = Ui_Eye_UI()
        # 初始化界面
        self.ui.setupUi(self)

        # 使用界面定义的控件，也是从ui里面访问

app = QApplication([])
mainw = MainWindow()
# mainw.show()
mainw.showFullScreen()
mainw.ui.label_eye.setText('<html><head/><body><p align="center"><span style=" font-size:5pt; font-weight:0; color:#ffffff;">E</span></p></body></html>')
app.exec_()