# since just showing image in OpenCV in notebook ipynb has the issue when closing the image, we should run the code as a script. In this code by pressing Esc, image is closed without error.
import cv2

path = '/Users/elmiraghahramani/Library/Mobile Documents/com~apple~CloudDocs/Online_courses/Python_for_CV_with_OpenCV_DL/Material/Computer-Vision-with-Python/DATA'
img = cv2.imread(path+'/00-puppy.jpg')

while True:
    
    cv2.imshow('Puppy', img) # window name = puppy

    if cv2.waitKey(1) & 0xFF == 27: # if we waited at least 1ms, AND we've pressed the Esc (symbol/number for Esc button)
        break

cv2.destroyAllWindows()
