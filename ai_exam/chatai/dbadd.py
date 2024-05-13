# 라이브러리 불러오기
import pymysql
from datetime import datetime
import requests 

#####################################################
# 데이터베이스 저장 함수
#####################################################

def ChatGPTadd(human_chat, ai_chat):
    # 데이터베이스 세팅
    conn = pymysql.connect(
        host = '127.0.0.1',
        # host = 'localhost' # 이거도 가능 하지만 인식을 못하는 경우도 가끔 있어서 위에거 쓰는게 좋음
        user = 'chat', 
        password='@ai1234@',
        port=3306,
        db='chatdb',
        charset='utf8'
    )

    try:
        # 현재 날짜 구하기
        saveDates= datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        # 아이피주소 확인
        saveIps = requests.get("http://ip.jsontest.com").json()['ip']
        
        cursor = conn.cursor()
        # insert 처리
        sql = "INSERT INTO chat (human_chat, ai_chat, dates, ips) VALUES(%s,%s,%s,%s)"
        val = (human_chat, ai_chat, saveDates, saveIps)
        cursor.execute(sql, val)
        conn.commit()
        print("데이터를 기록하였습니다.")

    except:
        print("입력 에러입니다.")
        
        
    conn.close()
