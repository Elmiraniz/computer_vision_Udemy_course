import numpy as np
import cv2
#____________________________________

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

prvsImg = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

hsv_mask = np.zeros_like(frame1)
hsv_mask[:,:,1] = 255

while True:
    ret, frame2 = cap.read()
    nextImg = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    
    flow = cv2.calcOpticalFlowFarneback(prvsImg, nextImg, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # flow gives x and y of the flow arrow in the direction of movement
    # we change it to polar coordinate to use it for HSV coloring
    
    mag, ang = cv2.cartToPolar(flow[:,:,0], flow[:,:,1], angleInDegrees=True) #flow: for each pixel, x and y
   
    hsv_mask[:,:,0] = ang/2
    hsv_mask[:,:,2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    
    bgr = cv2.cvtColor(hsv_mask, cv2.COLOR_HSV2BGR)
    cv2.imshow('Frame', bgr)
    
    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break
        
    prvsImg = nextImg
    
cap.release()
cv2.destroyAllWindows()