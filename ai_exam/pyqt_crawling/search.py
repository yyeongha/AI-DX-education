import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
from search_naver import *
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import *


searchMain = uic.loadUiType("ui/ui_crawling.ui")[0]

class SearchWin(QDialog, searchMain):
    # 전역변수
    searchKin = ''
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)       
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_add.clicked.connect(self.btn_add_clicked)
    
    def btn_add_clicked(self):
        # 리스트뷰에 데이터 추가
        model = QStandardItemModel()
        model.appendRow(QStandardItem('데이터 추가'))
        self.lv_search.setModel(self.model)
            
    def btn_save_clicked(self):
        if self.searchKin == '':
            QMessageBox.about(self, "에러", "검색한 정보가 없습니다.")
            return
        
        # 파일로 저장
        saveKin(f'search_file/{self.searchKin}')
            
    def btn_search_clicked(self):
        if self.le_search.text() == '':
            QMessageBox.about(self, "에러", "입력값이 존재하지 않습니다.")
            return
        
        naverClear()
        self.searchKin = self.le_search.text()
        # 검색 동작
        for i in range(10):
            page = i + 1
            naverKin(self.searchKin, page)
            print('#'*20 + ' ' + str(page) + ' ' + '#'*20)
            
            # # 리스트뷰에 보여주기 
            # model = QStandardItemModel()
            # for data in searchList:
            #     self.model.appendRow(QStandardItem(data[0]))
            # self.lv_search.setModel(model)
                
            time.sleep(1.5) # -> 랜덤으로 지정하면 기업에서 못잡음

    def btn_close_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()


