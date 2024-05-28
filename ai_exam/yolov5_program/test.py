# 라이브러리 설치
import torch

# 모델
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# 이미지 검증 (predict)
img = "https://cdn.mediatoday.co.kr/news/photo/202311/313885_438531_4716.jpg"

# 검증
results = model(img)

# 출력
results.print()  

# 프로그램에서 사용할 수 있도록 정보 받기 (화면에 이미지 출력)
results.show()

# 데이터 구조 형태로 보기
print(results.pandas().xyxy[0])

# savedata 폴더에 저장
results.save()

# crop
results.crop()