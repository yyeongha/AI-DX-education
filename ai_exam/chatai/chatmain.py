# openai 채팅 함수 불러오기
from chat import ChatMessage
from dbadd import ChatGPTadd

while True:
    msg = input("질문: ")
    rst = ChatMessage(msg)
    # db에 저장
    ChatGPTadd(msg, rst)
    print("답변: ", rst)
