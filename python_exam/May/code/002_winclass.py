import sys 
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,200,600,400)
        self.setWindowTitle("PyQT공부중...")

app = QApplication(sys.argv)
windowMain = MyWindow()
windowMain.show()
app.exec_()