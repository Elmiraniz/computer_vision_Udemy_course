import cv2
import time

cap = cv2.VideoCapture('DATA/mysupervideo.mp4')

if cap.isOpened() == False:
    print('Error file not found or wrong codec used!')
    
while cap.isOpened():
    
    ret, frame = cap.read()
    
    if ret == True:
        
        # same framerate of video
#         time.sleep(1/20) # only if wanna watch the video. 
        # this made my video look slower. without it the video played at normal speed
        cv2.imshow('FRAME', frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
            
    else: # if we are not getting any ret, all frames are shown
        break
        
cap.release()
cv2.destroyAllWindows()