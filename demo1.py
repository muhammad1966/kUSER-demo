import cv2

cap = cv2.VideoCapture(0)


kas, frame = cap.read()
cap.release()


img = cv2.imwrite('capImage.png', frame)

img2 = cv2.imread('capImage.png')

cv2.imshow('captured image', img2)
cv2.waitKey(0)
