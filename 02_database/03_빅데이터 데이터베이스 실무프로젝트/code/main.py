import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from mem_add import MemAddWin       # C
from memdb_list import MemDbList    # R
from mem_edit import MemEditWin     # U
from memdb_del import MemDbDel      # D

form_main = uic.loadUiType("ui/main.ui")[0]

class MyWindow(QMainWindow, form_main):
    del_idx = ''
    edit_idx = ''
    edit_mails = ''
    edit_names = ''
    edit_telnos = ''
    edit_addrs = ''
    edit_sns = ''

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.tbl_mem.cellClicked.connect(self.cellclicked_event)
        self.btn_del.clicked.connect(self.btn_del_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)

        # tbl_mem을 초기화
        self.tbl_mem.setColumnCount(6)
        self.tbl_mem.setHorizontalHeaderLabels(
            ["id", "mails", "names", "telnos", "addrs", "sns"]
        )

        # self.tbl_mem.setRowCount(0)

    def btn_edit_clicked(self):
        memEditWin = MemEditWin()
        # 데이터 전달 만들기
        memEditWin.loadData(
            self.edit_idx,
            self.edit_mails,
            self.edit_names,
            self.edit_telnos,
            self.edit_addrs,
            self.edit_sns
        )
        memEditWin.showModal()
        self.btn_search_clicked()

    def cellclicked_event(self, row, col):
        print(f"row = {row}, col = {col}")

        # 삭제
        self.del_idx = self.tbl_mem.item(row, 0).text()
        print("idx = ", self.del_idx)
        # 수정
        self.edit_idx       = self.tbl_mem.item(row, 0).text()
        self.edit_mails     = self.tbl_mem.item(row, 1).text()
        self.edit_names     = self.tbl_mem.item(row, 2).text()
        self.edit_telnos    = self.tbl_mem.item(row, 3).text()
        self.edit_addrs     = self.tbl_mem.item(row, 4).text()
        self.edit_sns       = self.tbl_mem.item(row, 5).text()

    def btn_del_clicked(self):
        if self.del_idx == '':
            QMessageBox.about(self, '확인', '선택된 항목이 없습니다.')
            return

        # 삭제하기
        if MemDbDel(self.del_idx) == True:
            QMessageBox.about(self, '확인', '데이터를 삭제하였습니다.')
            self.btn_search_clicked()
        else:
            QMessageBox.about(self, '에러', '데이터 삭제에 실패하였습니다.')
        
        self.del_idx = ''

    def btn_search_clicked(self):
        # 데이터 조회 결과 처리
        datas = MemDbList(self.le_search.text())
        print('데이터크기 : ', len(datas))
        self.tbl_mem.setRowCount(len(datas))
        
        # 데이터 적용
        for idx, data in enumerate(datas):
            self.tbl_mem.setItem(idx,0,QTableWidgetItem(str(data[0])))
            self.tbl_mem.setItem(idx,1,QTableWidgetItem(data[1]))
            self.tbl_mem.setItem(idx,2,QTableWidgetItem(data[2]))
            self.tbl_mem.setItem(idx,3,QTableWidgetItem(data[3]))
            self.tbl_mem.setItem(idx,4,QTableWidgetItem(data[4]))
            self.tbl_mem.setItem(idx,5,QTableWidgetItem(data[5]))

    def btn_add_clicked(self):
        memAddWin = MemAddWin()
        memAddWin.showModal()
        self.btn_search_clicked()

    def btn_close_clicked(self):
        exit()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()