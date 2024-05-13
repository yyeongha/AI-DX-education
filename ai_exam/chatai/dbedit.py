# 만들어놓은 데이터베이스의 데이터를 조회

# 라이브러리 불러오기
import pymysql

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
    cursor = conn.cursor()
    sql = """UPDATE chat 
          set human_chat = %s,
              ai_chat =  %s,
              dates = %s,
              ips = %s
          WHERE id = %s"""
    val = [
        ('테스트','테스트 답변','2023-01-01','9.9.9.9',5),
        ('테스트','테스트 답변','2023-01-01','9.9.9.9',6)
        ]
    cursor.executemany(sql, val)
    conn.commit()

except:
    print("업데이트 에러입니다.")
    
conn.close()
