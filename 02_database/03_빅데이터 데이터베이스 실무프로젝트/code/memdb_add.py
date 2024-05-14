# 라이브러리 불러오기
import pymysql
from datetime import datetime
import requests

#######################################################
# 데이터베이스 저장 함수
#######################################################

def MemDbAdd(mails, names, telnos, addrs, sns):
    # 데이터베이스 셋팅
    conn = pymysql.connect(
        host='127.0.0.1',
        # host='localhost',
        user='mem',
        password='@ai1234@',
        port=3306,
        db='memdb',
        charset='utf8'
    )

    # try:
    # 현재 날짜 구하기
    saveDates = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    # 아이피주소 확인
    saveIps = requests.get("http://ip.jsontest.com").json()['ip']
    cursor = conn.cursor()
    # insert 처리
    sql = """INSERT INTO member 
    (mails, names, telnos, addrs, sns, date_created, ips) 
    VALUES 
    (%s, %s, %s, %s, %s, %s, %s)"""
    val = (mails, names, telnos, addrs, sns, 
        saveDates, saveIps)
    cursor.execute(sql, val)
    conn.commit()
    print("데이터를 기록하였습니다.")
    # except:
    #     print("입력 에러입니다.")

    conn.close()

# MemDbAdd(
#     'test@nanver.com', 
#     '홍길동', 
#     '000-0000-0000', 
#     '서울시 강남구', 
#     'facebook')
