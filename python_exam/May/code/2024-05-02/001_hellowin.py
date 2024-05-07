import sys 
from PyQt5.QtWidgets import *

app = QApplication(sys.argv) # 윈도우 만듦

btn = QPushButton("푸시버튼입니다.") # 윈도우 안 버튼 만듦
btn.show() # 화면이 보임

app.exec_() # 사용자가 종료버튼을 누르기 전까지 프로그램 동작


