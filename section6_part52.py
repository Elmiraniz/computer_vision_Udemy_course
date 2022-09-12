import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
####################################


def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255) # we make tuples, just like rgb tuples (r, g, b)
# in CV2 we need to change to BGR but here we are just concerned about the colors being different

colors = []
for i in range(10):
    colors.append(create_rgb(i))
    
    
road = cv2.imread('DATA/road_image.jpg')
road_copy = road.copy()

marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)


# Callback code

# Global vars
# Color choice
n_markers = 10 # 0-9
current_marker = 1

#Markers updated by watershed
marks_updated = False


# Callback func

def mouse_callback(event, x, y, flags, param):
    global marks_updated
    
    if event == cv2.EVENT_LBUTTONDOWN:
        # Markers passed to watershed
        cv2.circle(marker_image, (x,y), 10, (current_marker), -1)
        
        # User sees on the road image
        cv2.circle(road_copy, (x,y), 10, colors[current_marker], -1)
        
        marks_updated = True
        
# While Trure
cv2.namedWindow('Road image')
cv2.setMouseCallback('Road image', mouse_callback)

while True:
    cv2.imshow('Watershed segments', segments)
    cv2.imshow('Road image', road_copy)
    
    k = cv2.waitKey(1)
    
    # Close all windows
    if k == 27:
        break
        
    # Clear all the colors on pressing C
    elif k == ord('c'):
        road_copy = road.copy()
        marker_image = np.zeros(road.shape[:2], dtype=np.int32)
        segments = np.zeros(road.shape, dtype=np.uint8)
        
    # update color choice
    elif k > 0 and chr(k).isdigit(): # chr(k) changes k to its actual number (in char) we clicked on keyboard
        current_marker = int(chr(k)) # i.e. change char 2, to int 2
        
    # Update the markings
    if marks_updated:
        marker_image_copy = marker_image.copy()
        cv2.watershed(road, marker_image_copy)
        
        segments = np.zeros(road.shape, dtype=np.uint8)
        
        for color_ind in range(n_markers):
            # Coloring the segments
            segments[marker_image_copy == (color_ind)] = colors[color_ind]
        
cv2.destroyAllWindows()