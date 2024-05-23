# opencv 버전 확인
import cv2

print(cv2.__version__)

# 원본 호출
org_image = cv2.imread("hellokitty.jpg", cv2.IMREAD_COLOR)
cv2.imshow("hellokitty.jpg", org_image) # imshow : 이미지를 창에 표시

# 이미지 가공
grey_image = cv2.imread("hellokitty.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("hellokitty.jpg", grey_image) # imshow : 이미지를 창에 표시

cv2.waitKey() # waitKey : 키 입력이 있을 때까지 무한정 대기
cv2.destroyAllWindows() # destroyAllWindows : 모든 창을 닫음
