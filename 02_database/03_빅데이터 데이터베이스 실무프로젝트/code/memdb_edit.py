# 라이브러리 불러오기
import pymysql

def MemDbEdit(idx, mails, names, telnos, addrs, sns):
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

    cursor = conn.cursor()

    sql = """
        UPDATE member 
        set mails = %s, 
            names = %s, 
            telnos = %s, 
            addrs = %s,
            sns = %s
        WHERE id = %s
        """
    val = [mails, names, telnos, addrs, sns, idx]
    cursor.execute(sql, val)
    conn.commit()


    conn.close()