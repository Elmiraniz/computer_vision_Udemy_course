import numpy as np
import cv2

corner_track_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)
# maxCorner: max number of points to track

lk_params = dict(winSize=(200,200), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10,0.03)) # LK params
# larger window: tracks faster movements, not sensitive to small movement
# smaller window: can't track faster movements, sensitive to small movement

# Level: LK uses image pyramid in its methods. Each level corresponds to a resolution. Level2=res. 1/(2^level)=1/4
# Image pyramid: signal or an image is subject to repeated smoothing and subsampling. 

# criteria EPS: epsilon choice (here 0.03) which exchanges speed vs. accuracy or our tracking.
# smaller epsilon ends tracking sooner.
# Criteria count: number of iterations (here 10)

cap = cv2.VideoCapture(0)

ret, pre_frame = cap.read()

pre_gray = cv2.cvtColor(pre_frame, cv2.COLOR_BGR2GRAY)

# Points to track
prevPts = cv2.goodFeaturesToTrack(pre_gray, mask=None, **corner_track_params)

mask = np.zeros_like(pre_frame) # for visualizing

while True:
    
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    nextPts, status, err = cv2.calcOpticalFlowPyrLK(pre_gray, frame_gray, prevPts, None, **lk_params)
    # status returns a vector that contains ones where it has found optical flow for the corresponding features
    # we're tracking max 10 points here, as defined in dictionary lk_params
    
    # Connecting the previous points to next points
    good_new = nextPts[status==1]
    good_pre = prevPts[status==1]
    
    for i, (new,prev) in enumerate(zip(good_new, good_pre)):
        
        x_new, y_new = new.ravel() # flatens a matrix, same as reshape(-1, order=order)
        x_prev, y_prev = prev.ravel()
        x_new = int(x_new)
        y_new = int(y_new)
        x_prev = int(x_prev)
        y_prev = int(y_prev)

        
        mask = cv2.line(mask, (x_new,y_new), (x_prev,y_prev), (0,255,0), 3)
        
        frame = cv2.circle(frame, (x_new,y_new), 8, (0,0,255), -1)
    
    img = cv2.add(frame, mask)
    cv2.imshow('Tracking', img)
    
    k = cv2.waitKey(30) & 0xFF
    if k==27:
        break
        
    prev_gray = frame_gray.copy()
    prevPts = good_new.reshape(-1,1,2) # change to the format accepted by cv2.goodFeaturesToTrack

    
cv2.destroyAllWindows()
cap.release()
    
    
    
    
    