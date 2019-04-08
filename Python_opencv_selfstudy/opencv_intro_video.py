import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

while(True):
    #capture frame-by-frame
    ret, frame = cap.read()
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()

#display video from file
cap = cv.VideoCapture('Video/test_video.avi')
#the the value of fps
fps = cap.get(cv.CAP_PROP_FPS)
fps_set = int(1/int(fps)*1000)
print('the fps from the test video is: ' + str(fps_set))

while(cap.isOpened()):
    ret, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(fps_set -4) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()