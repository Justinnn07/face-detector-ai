# Importing cv2 dependency
import cv2 
from random import randrange
import os
import sys
import subprocess
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Importing Image
# img = cv2.imread("Images.jpg")
# img = cv2.imread("download (4).jpg")

webcam = cv2.VideoCapture(0)

while True:
    successfull_frame_read, frame = webcam.read()
    
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Detect Faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
     cv2.rectangle(frame,(x, y), (x+w, y+h), (randrange(128,256), randrange(256), 0), 4)
# To show
    cv2.imshow("Justin's Face detector", frame)
    

# to play
    key = cv2.waitKey(1)
    if key==81 or key==113:
        break
webcam.release()

try:
    subprocess.Popen('explorer "Bill Records"')
except Exception as e:
    print(e)

print("CODE COMPLETED")
