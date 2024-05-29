# 라이브러리 불러오기
import cv2
import torch
import yolov5
import pandas as pd
import yaml
import time

import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

# yolov5 custom model 불러오기
model = torch.hub.load(
    'ultralytics/yolov5', 
    'custom', 
    path='./train/best.pt', 
    force_reload=False
    )

# yaml에 있는 데이터셋(labels) 불러오기
data_yaml = './train/data.yaml'

with open(data_yaml) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

# print(data)
# print(data['names'])

# 라벨(정답)처리
labels = data['names']
print(labels)

# 어디서 가져올것인가(소스)
cap = cv2.VideoCapture(0) # 0 : 카메라가 하나일 경우, 그 카메라(첫번째 카메라)를 제어함

# 카메라 크기 조정
cap.set(3, 1280)
cap.set(4, 720)

# 실시간으로 계속 영상 받기
while True:
    _, frame = cap.read()
    
    # 원본영상
    frame = cv2.flip(frame, 1)
    
    # yolov5 처리 후
    results = model(frame)
    
    df_hand = results.pandas().xyxy[0]
    hands = df_hand.values.tolist()
    
    for hand in hands:
        print("손인식: ", hand[6])
    
    labels = results.xyxyn[0][:, -1].cpu.numpy()
    bbox = results.xyxyn[0][:, :-2].cpu.numpy()
    score = results.xyxyn[0][:, -2].cpu.numpy()
        
    print("labels= ", labels)
    print("bbox= ", bbox)
    print("score= ", score)
    
    # 바운딩박스 처리
    if len(labels) > 0:
        # 네모박스 INT 처리
        x1 = int(bbox[0][0])
        y1 = int(bbox[0][1])
        x2 = int(bbox[0][2])
        y2 = int(bbox[0][3])
    
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2) # 사각형 그리기, 2는 선의 두께
        
    cv2.imshow('camera', frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


