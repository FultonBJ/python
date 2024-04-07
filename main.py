import numpy as np
import cv2 as cv
import sys


PREVIEW = 0
BLUR = 1
FEATURES = 2
CANNY = 3

feature_params = dict(maxCorners = 5000, qualityLevel = 0.2, minDistance = 15, blockSize =9)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]
    
    image_filter = PREVIEW
    alive = True
    
win_name = 'Camera_Filters'
cv.namedWindow(win_name, cv.WINDOW_NORMAL)
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot Open Camera")
    exit()
    
while cv.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    cv.imshow(win_name, frame)

    
while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break
    frame = cv.flip(frame,1)
    
    if image_filter ==PREVIEW:
        result=frame
  
    

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break
    # Our operations on the frame come here
    color = cv.cvtColor(frame, cv.COLOR_BGR2BGRA)
  
    # Display the resulting frame
    cv.imshow('frame', color)
    cv.imcount('frame', 10)
     
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture

cap.release()
cv.destroyAllWindows()
