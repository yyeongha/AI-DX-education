import sys 
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtGui import *

import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def clean_text(inputString):
    text_rmv = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’\'·]', ' ', inputString)
    return text_rmv

path = "./search_file/"

# 워드클라우드 자동 저장 함수
def wordCloudSView():
    # listdir 은 현재 경로에 있는 모든 파일을 확인
    file_list = os.listdir(path)
    fileList1 = [file for file in file_list if file.endswith('.csv')]
    
    #  배열의 여러 csv 파일을 자동 병합해서 하나의 df 파일로 만드는 처리
    dfCsv = pd.DataFrame()
    for i in fileList1:
        data = pd.read_csv(path + i, encoding='utf-8')
        dfCsv = pd.concat([dfCsv,data])

    dfCsv = dfCsv.reset_index(drop=True)
    
    # dataframe에서 링크를 제거 (drop)
    dfCsv = dfCsv.drop(['링크'], axis='columns')
    
    # pandas 형식 -> list
    listCsv = dfCsv['제목'].astype(str).tolist()
    
    # 리스트 문자열을 하나의 문자열로 만드는 방법
    wordStr = ' '.join(listCsv)
    
    # 문자열 걸러내기
    wordStr = clean_text(wordStr)
    
    wc1 = WordCloud(
    font_path = "c:Windows\fonts\malgun.ttf",
    stopwords = ["알리익스프레스", "알리", "익스프레스", "테무", "쇼핑몰"],
    background_color = 'white',
    width = 501,
    height = 273,
    random_state = 40,)
    
    # 워드 클라우드에 우리가 생성한 단어를 적용
    wc1.generate(wordStr)

    # 이미지로 저장
    wc1.to_file("search_file/word.png")
        

wordMain = uic.loadUiType("ui/ui_wordcloud.ui")[0]

class WordWin(QDialog, wordMain):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_wordcloud.clicked.connect(self.btn_wordcloud_clicked)
        
    def btn_wordcloud_clicked(self):
        wordCloudSView()
        # 불러오기
        self.lb_img.setPixmap(QPixmap('./search_file/word.png')) 

    def btn_close_clicked(self):
        self.close()

    def showModal(self):
        return super().exec_()


