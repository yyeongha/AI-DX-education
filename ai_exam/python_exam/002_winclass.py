import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,600,400)
        self.setWindowTitle("PyQT공부중...")
        self.setWindowIcon(QIcon("icon.png"))

        btn = QPushButton("버튼1", self)
        btn.clicked.connect(self.btn_click)

    def btn_click(self):
        print("버튼을 눌렀습니다.")

app = QApplication(sys.argv)
windowMain = MyWindow()
windowMain.show()
app.exec_()