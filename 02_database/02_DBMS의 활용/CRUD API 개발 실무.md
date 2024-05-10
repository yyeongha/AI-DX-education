title: CRUD API 개발 실무

## 서버 (ubuntu)
* home\ai 경로에 오른쪽 마우스 => new folder -> chatai 만들기
![newfolder]()

## vscode 
* extension : Remote developemet 설치
* comment palette -> remote-ssh connect to host -> ssh ai@192.168.56.1 -> linux -> 비번 

* open folder -> home/ai/ai/chatai -> test.py 파일 생성 -> python extension 설치
=> 원격 서버의 파이썬 사용

* terminal 
ai@Ubuntu22:~/ai/chatai$ 이렇게 뜸

```
python3 -m venv venv # venv 폴더 생김
```

* select interpreter -> 3.10.12 venv 선택 -> 터미널 끄고 새로 키면 앞에 venv가 앞에 뜸 
![newterminal]()

* teminal
```
pip install openai
```
-> openai가 venv에 들어감
-> venv\lib\ 에서 설치된거 볼 수 있음


## new file -> chat.py  
* pip install openai==0.28

* chat.py 파일 생성
# 1. 라이브러리 등록
import openai


# 2. 환경설정

```
# openai 키등록
OPENAI_KEY = "input your openapi key"
openai.api_key = OPENAI_KEY

# 3. 인공지능 모델 선택
MODEL = "gpt-3.5-turbo"

##############################################################
# chatgpt 함수
##############################################################
def ChatMessage(msg):
    response = openai.ChatCompletion.create(
        model = MODEL,
        messages = [
            {"role":"system", "content":"대답을 자세히 해주세요."},
            {"role":"user", "content":msg},
            {"role":"assistant","content":""}
        ],  
        temperature=0
    )

    print(response)
    return response['choices'][0]['message']['content']
```
* 질문: 생성형 ai에 대해 알려줘
![question]()

* 만약 
![change]()
이거로 바꾼다면 

![answer]()


* chatmain.py 생성


## erd cloud
create erd 
title : chatbot
add new entity

![erd]()






