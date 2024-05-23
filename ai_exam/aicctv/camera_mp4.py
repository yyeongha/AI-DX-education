# 라이브러리 불러오기
import cv2

# 어디서 가져올것인가(소스)
cap = cv2.VideoCapture(0) # 0 : 카메라가 하나일 경우, 그 카메라(첫번째 카메라)를 제어함


# 실시간으로 계속 영상 받기
while True:
    _, frame = cap.read()
    
    # 프레임 정보
    print("현재진행프레임 : ", cap.get(cv2.CAP_PROP_POS_FRAMES))
    print("현재전체프레임 : ", cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # mp4 영상
    cv2.imshow('newjeans.mp4', frame)
    
    # 영상을 흑백으로 전환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BAYER_BG2GRAY)
    cv2.imshow('gray camera', gray_frame)
    
    if cv2.waitKey(1) & 0xFf == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
        