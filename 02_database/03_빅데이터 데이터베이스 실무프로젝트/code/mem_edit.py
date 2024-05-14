import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

from memdb_edit import MemDbEdit

memEditMain = uic.loadUiType("ui/mem_edit.ui")[0]

class MemEditWin(QDialog, memEditMain):
    edit_idx = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)

    def loadData(self, idx, mails, names, telnos, addrs, sns):
        self.edit_idx = idx
        self.le_mails.setText(mails)
        self.le_names.setText(names)
        self.le_telnos.setText(telnos)
        self.le_addrs.setText(addrs)
        self.le_sns.setText(sns)

    def btn_edit_clicked(self):
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
            MemDbEdit(
                self.edit_idx,
                self.le_mails.text(),
                self.le_names.text(),
                self.le_telnos.text(),
                self.le_addrs.text(),
                self.le_sns.text()
            )
            QMessageBox.about(self, '수정완료', '수정되었습니다.')
        except:
            QMessageBox.about(self, '수정에러', '수정에 실패하였습니다.')

    def btn_close_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()