import cv2
import numpy as np

###################
###### Function ###
###################

def draw_circle(event, x, y, flags, param):
    
    if event == cv2.EVENT_LBUTTONDOWN: # right when the left button is pressed down before releasing
        # what should the program do when left button is pushed down:
        cv2.circle(img, (x,y), 100, (0,255,0), -1) # radius=100, color, filled circle       

    elif event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x,y), 100, (255, 0, 0), -1) # rgb color in CV: bgr
        
# connect the window to the function
cv2.namedWindow(winname = 'my_drawing')
cv2.setMouseCallback('my_drawing', draw_circle) # we're not calling the func, just passing it to the call back.

###################
###Showing image with OpenCV
############################

img = np.zeros((512, 512, 3), np.int8)

# For closing figure without error in Mac/Linux
while True:
    cv2.imshow('my_drawing', img)

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
