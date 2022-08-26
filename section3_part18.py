import cv2
import numpy as np

#### Variables
drawing = False # not drawing (when mouse button up). True when mouse button down
ix = -1
iy = -1



#### Function
# draws rectangle if we constantly get further away in both directions from the initial point
def draw_rectangle(event, x, y, flags, params):

    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix,iy), (x,y), (0,255,0), -1)



#### Showing image
img = np.zeros((512,512,3))

cv2.namedWindow(winname='my_drawing')

cv2.setMouseCallback('my_drawing',draw_rectangle)


# For closing the figure with ESC key

while True:

    cv2.imshow('my_drawing', img)

    # check for ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
