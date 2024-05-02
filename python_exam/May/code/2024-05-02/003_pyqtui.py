import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_main = uic.loadUiType("main.ui")[0]

class MyWindow(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn1.clicked.connect(self.btn1_clicked)
        # self.btn2.clicked.connect(self.btn2_clicked)
        self.btn2.clicked.connect(self.btn2_ok)

    def btn1_clicked(self):
        print("버튼1클릭")
        QMessageBox.about(self, "메세지창", "버튼1이 눌러졌습니다.")

    # def btn2_clicked(self):
    #     print("버튼2클릭")
    
    def btn2_ok(self):
        btnQa = QMessageBox.information(
            self,
            "삭제",
            "자료를 삭제하겠습니까?",
            QMessageBox.Yes | QMessageBox.Cancel
        )

        if btnQa == QMessageBox.Yes:
            QMessageBox.about(self, "삭제완료", "자료를 삭제하였습니다.")
        if btnQa == QMessageBox.Cancel:
            QMessageBox.about(self, "삭제취소", "취소하였습니다.")

    

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()