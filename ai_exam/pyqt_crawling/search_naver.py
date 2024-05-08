####################################################################################
# 네이버 지식인 자동 크롤링 프로그램
# 일자 : 2024년 5월 7일
# lib : requests, beautifulsoup4, selenium
####################################################################################

# 라이브러리 사용
import csv
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus
import requests
import codecs
import time

# csv로 저장할 배열
searchList = []

def naverClear():
    global searchList
    searchList = []

def naverKin(search, i):
    # url에서 정보 가져오기
    url = f"https://kin.naver.com/search/list.naver?query={quote_plus(search)}&page={i}"

    # 인터넷에서 정보 가져오기(requests)
    html = requests.get(url)
    print(html)

    # 만약 응답코드가 200이 아니면 종료
    if html.status_code == 200:
        htmlcode = html.text
        print(htmlcode)
        # 선언
        soup = bs(htmlcode, 'html.parser')
        # <ul class="basic1"> 찾는과정
        ul = soup.select_one("ul.basic1")
        # li 추출
        titles = ul.select('li>dl>dt>a')
        
        # 데이터 값 가져오기
        for title in titles:
            print(title.text)
            print(title.attrs['href'])
            
            # 임시 공간에 저장
            tmp = []
            tmp.append(title.text)
            tmp.append(title.attrs['href'])
            searchList.append(tmp)
            
            return searchList

def saveKin(search):
    # 파일로 저장
    f = codecs.open(f'{search}.csv', 'w', encoding='utf-8')
    
    csvWriter = csv.writer(f)

    csvWriter.writerow(['제목', '링크'])

    for data in searchList:
        # 한줄씩 저장
        csvWriter.writerow(data)

    f.close()
    
####################################################################################
# 함수 테스트
####################################################################################

# search = input("검색어: ")
# for i in range(10):
#     page = i + 1
#     naverKin(search, page)
#     print('#'*20 + ' ' + str(page) + ' ' + '#'*20)
#     time.sleep(1.5)
    