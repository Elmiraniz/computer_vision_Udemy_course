import cv2
import numpy as np

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(im, (x,y), 100, (0,0,255), 10)

        
path = '/Users/elmiraghahramani/Documents/GitHub/computer_vision_Udemy_course/DATA/'
im = cv2.imread(path+'dog_backpack.jpg')

cv2.namedWindow(winname = 'new_image')
cv2.setMouseCallback('new_image', draw_circle)

while True:
    
    cv2.imshow('new_image',im)
#     if cv2.waitKey(20) & 0xFF == 113: 
    if cv2.waitKey(20) == ord('q'): # this will wait for 'q' button to exit image. 
        break
        
cv2.destroyAllWindows()