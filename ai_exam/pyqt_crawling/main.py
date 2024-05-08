import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic

from search import SearchWin
from word import WordWin

form_main = uic.loadUiType("ui/ui_main.ui")[0]

class MyWindow(QMainWindow, form_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_wordcloud.clicked.connect(self.btn_wordcloud_clicked)
        
    def btn_wordcloud_clicked(self):
        wordWin = WordWin()
        wordWin.showModal()
            
    def btn_search_clicked(self):
        searchWin = SearchWin()
        searchWin.showModal()  

    def btn_close_clicked(self):
        exit()

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()