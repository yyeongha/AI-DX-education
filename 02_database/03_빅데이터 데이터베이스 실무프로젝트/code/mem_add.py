import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from memdb_add import MemDbAdd

memAddMain = uic.loadUiType("ui/mem_add.ui")[0]

class MemAddWin(QDialog, memAddMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)

    def btn_add_clicked(self):
        # 에러처리에 대한 부분
        if self.le_mails.text() == '':
            QMessageBox.about(self, '입력에러', '메일주소를 입력하세요.')
            return
        if self.le_names.text() == '':
            QMessageBox.about(self, '입력에러', '이름을 입력하세요.')
            return
        if self.le_telnos.text() == '':
            QMessageBox.about(self, '입력에러', '전화번호를 입력하세요.')
            return
        if self.le_addrs.text() == '':
            QMessageBox.about(self, '입력에러', '주소를 입력하세요.')
            return
        
        try:
        # 데이터 저장
            MemDbAdd(
                self.le_mails.text(),
                self.le_names.text(),
                self.le_telnos.text(),
                self.le_addrs.text(),
                self.le_sns.text()
            )
            QMessageBox.about(self, '등록완료', '등록되었습니다.')
        except:
            QMessageBox.about(self, '입력에러', '데이터베이스에 입력이 실패하였습니다.')

    def btn_close_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()