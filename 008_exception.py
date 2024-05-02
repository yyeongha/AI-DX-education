try:
    x = input("숫자를 입력하세요:") # 입력받을때 x가 str으로 받음

    y = 10 / int(x) # 그래서 int로 바꿔야함
    print(y)

except:
    print("숫자는 0으로 나눌 수 없습니다.")


# 숫자를 0으로 입력했을 때
# ZeroDivisionError: division by zero
    
# try exception을 이용하면 except에서 에러 메시지가 나옴
