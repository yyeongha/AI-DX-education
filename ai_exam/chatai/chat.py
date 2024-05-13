# 1. 라이브러리 등록
import openai


# 2. 환경설정
# openai 키등록
OPENAI_KEY = "put your api key!"
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
            {"role":"system", "content":"질문에 대답을 경상도 사투리로 답변해줘"},
            {"role":"user", "content":msg},
            {"role":"assistant","content":""}
        ],  
        temperature=0
    )

    print(response)
    return response['choices'][0]['message']['content']


