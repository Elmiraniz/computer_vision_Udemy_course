import cv2
import numpy as np
import matplotlib.pyplot as plt
#================================

# Wanna get detect the frontal face. 
# It might find faces not looking toward the camera, but it doesn't have a good performance for it
face_cascade = cv2.CascadeClassifier('DATA/haarcascades/haarcascade_frontalface_default.xml')
#================================

def detect_face(img):
    
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img) # x, y, width, height
    
    for (x,y,w,h) in face_rects:
        cv2.rectangle(face_img, (x,y), (x+w,y+h), (255,255,255), 10)
    
    return face_img
#================================

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read(0)
    
    frame = detect_face(frame)
    
    cv2.imshow('Video face detector', frame)
    
    k = cv2.waitKey(1)
    
    if k == 27:
        break
        
cap.release()
cv2.destroyAllWindows()
