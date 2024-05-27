# django 서비스에 db 연결하기
* vscode
open folder > aiwebcam > settings.py 생성

## 1. 프로젝트 경로
d:\ai_exam\ai_webcam

## 2. 가상환경 생성
-> 기존 가상환경 사용
p312_aiwebcam

## 3. 라이브러리 설치 (django) - vscode 터미널
```
pip install django==4.0
pip install opencv-python
pip install pillow
conda install -c conda-forge dlib
pip install matplotlib
```

* 실행 - vscode 터미널
python manage.py runserver

pip install mysqlclient

ctrl + c

<장고 데이터베이스 초기화(생성)> - vscode 터미널
python manage.py migrate


## ssh 터미널에서 
use yangdb;
show tables;

<테이블 생성하는 방법>
/web/models.py

<데이터베이스 생성 여부 확인> - vscode 터미널
python manage.py makemigrations web 
python manage.py migrate


http://localhost/web/adduser/
=> 데이터베이스에 저장

python manage.py runserver
http://localhost/web/adduser/













