## 데이터베이스 생성
- IP : 192.168.56.1
- ID : chat
- DB : chatdb
- PW : @ai1234@
- root id, pw


## vscode에서 sql 들어가서 작업
```
# 데이터베이스 접속
su -
mysql -u root -p

# 데이터베이스가 무엇있는지 확인하는 명령
show databases;

# 데이터베이스를 선택 명령
use mysql;

# 데이터베이스 생성
create database chatdb;

# 사용자를 생성
create user 'chat'@'localhost' identified by '@ai1234@';
create user 'chat'@'%' identified by '@ai1234@';

# 데이터베이스를 사용할 사용자 권한을 부여
grant all privileges on chatdb.* to 'chat'@'localhost';
grant all privileges on chatdb.* to 'chat'@'%';

# 권한적용
flush privileges;

exit;

# 만들어진거 확인
mysql -u chat -p chatdb
```

![maria]()


## 내 컴퓨터로 강사님 컴퓨터 원격 접속하는 법
cmd에서 ipconfig

ssh ai@192.168.0.47 로 들어가서 비번 치면 됨


## MySQL workbench 제작
### set up new connection

![mysqlworkbench]()


### erd cloud에서 코드 복사

![erdcloud2]()

### mysql에 수정해서 복붙
* int, PRIMARY KEY 추가
![copypaste]()


### columms 기록
* 기록 ->  apply -> apply
![columns]()
![apply]()


## python으로 mysql에 사용하기
* pymysql 설치

```
pip install pymysql
```

![installpymysql]()

* dbqry.py 파일 만들기
```
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

conn.close()
```

