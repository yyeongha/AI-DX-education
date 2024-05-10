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

