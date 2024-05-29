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
    force_reload=True
    )

# yaml에 있는 데이터셋(labels) 불러오기
data_yaml = './train/data.yaml'

with open(data_yaml) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)

print(data)
print(data['names'])