import cv2

cap = cv2.VideoCapture(0) # grabs default camera

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Windows:  *'DIVX'
# MACOS or Linux: *'XVID'

writer = cv2.VideoWriter('DATA/mysupervideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width,height))

while True:
    
    ret, frame = cap.read() # tuple unpacking
    
    # Here we can put operations like track object, etc
    writer.write(frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray) # if we wanna see the full color image, we comment out the top line, and imshow('frame',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.realease()
writer.release()
cv2.destroyAllWindows()