# 라이브러리 불러오기
import pymysql

def MemDbDel(idx):
    if idx == '':
        return False
    
    # 데이터베이스 셋팅
    conn = pymysql.connect(
        host='127.0.0.1',
        # host='localhost',
        user='mem',
        password='input your password',
        port=3306,
        db='memdb',
        charset='utf8'
    )

    try:
        cursor = conn.cursor()

        sql = "DELETE FROM member WHERE id = %s"
        val = idx
        cursor.execute(sql, val)
        conn.commit()
    except:
        conn.close()
        print("삭제 에러입니다.")
        return False
    finally:
        conn.close()

        return True