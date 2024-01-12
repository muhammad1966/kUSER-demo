import cv2
import face_recognition
import random
import os


cap = cv2.VideoCapture(0)


kas, frame = cap.read()
cap.release()


img = cv2.imwrite('capImage.png', frame)

img1 = cv2.imread('muhd.jpg')
img2 = cv2.imread('capImage.png')


image1 = face_recognition.face_encodings(img1)[0]
image2 = face_recognition.face_encodings(img2)[0]

result = face_recognition.compare_faces([image1], image2)

if result:
    print(True)
    os.remove('capImage.png')
else:
    print(False)


