# 라이브러리 불러오기
import pymysql

def MemDbList(qry):
    rst = ''

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

        if qry == '':
            sql = "select id, mails, names, telnos, addrs, sns from member"
        else:
            sql = f"""select id, mails, names, telnos, addrs, sns
            from member 
            where 
            (mails like '%{qry}%' or
            names like '%{qry}%' or
            telnos like '%{qry}%' or
            addrs like '%{qry}%' or
            sns like '%{qry}%')
            """
        cursor.execute(sql)
        rst = cursor.fetchall()
        for data in rst:
            print(data)

        # conn.close()
        # return rst
    except:
        print("조회 에러입니다.")
    finally:
        conn.close()

        return rst

# 데이터 조회
# data = MemDbList('2222')
# print('data = ', data)