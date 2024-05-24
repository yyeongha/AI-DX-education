from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse

# opencv 라이브러리 불러오기
import dlib
import cv2
import matplotlib.patches as patches
import numpy as np

class FaceDetector:
    def __init__(self):
        self.
        self.image = None
        self.detections = None

    def load_image(self, image):
        self.image = image

    def detect_faces(self, upsample_num_times=1):
        if self.image is None:
            raise ValueError("Image not loaded.")
        self.detections = self.detector(self.image, upsample_num_times)

    def draw_faces(self):
        if self.detections is None:
            raise ValueError("No faces.")
        for det in self.detections:
            x, y, w, h = det.left(), det.top(), det.width(), det.height()
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            
# 실시간 영상에서 얼굴 검출 예시
if __name__ == "__main__":
    predictor_path = "./trained/shape_predictor_68_face_landmarks.dat"

    face_detector = FaceDetector(detector_path="", predictor_path=predictor_path)

    # 영상 소스 가져오기 (카메라를 사용)
    cap = cv2.VideoCapture(0)

    # 카메라 크기 조정
    cap.set(3, 1280)
    cap.set(4, 720)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 원본 영상 (좌우 반전)
        frame = cv2.flip(frame, 1)
        
        # Dlib을 사용하여 얼굴 검출
        face_detector.load_image(frame)
        face_detector.detect_faces()

        # 얼굴을 프레임에 그림
        face_detector.draw_faces()

        # OpenCV를 사용하여 원본 영상 표시
        cv2.imshow('camera', frame)

        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    

def video_feed(request):
    return StreamingHttpResponse(stream(),
    content_type='multipart/x-mixed-replace;boundary=frame')

# 영상을 보내는 함수
def stream():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 인식할 수 없습니다.")
            break
        
        # 얼굴인식 처리 여기에 넣으면 됨

        # 서버로 데이터를 전송
        # 이미지를 binary 웹에서 전송이 가능한 형태
        image_bytes = cv2.imencode('.jpg',frame)[1].tobytes()
        # 서버로 전송
        yield(b'--frame\r\n'
        b'Content-type:image/jpeg\r\n\r\n' + image_bytes
        + b'\r\n')

# Create your views here.
def index(request):
    return render(request, 'webcam_main.html')