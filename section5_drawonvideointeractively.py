import cv2

## CAllback function rectangle
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, topLeft_clicked, botRight_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if topLeft_clicked and botRight_clicked: # Reset the drawn rectangle
            pt1 = (0, 0)
            pt2 = (0, 0)
            topLeft_clicked = False
            botRight_clicked = False

        if not topLeft_clicked:
            pt1 = (x, y)
            topLeft_clicked = True

        elif not botRight_clicked:
            pt2 = (x, y)
            botRight_clicked = True


## Global variables
pt1 = (0, 0)
pt2 = (0, 0)
topLeft_clicked = False
botRight_clicked = False
## Connect to the callback
cap = cv2.VideoCapture(0)
cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:
    ret,  frame = cap.read()

    # draw on frame
    if topLeft_clicked:
        cv2.circle(frame, center=pt1, radius=5,color=(0,0,255),thickness=-1)

    if topLeft_clicked and botRight_clicked:
        cv2.rectangle(frame, pt1, pt2, (0,0,255), 3)


    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
