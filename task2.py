import numpy as np
import cv2 as cv
cap = cv.VideoCapture('input.mp4')
i = 1
while cap.isOpened():
    ret, frame = cap.read()
    if i%4==0:
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        cv.imshow('frame', frame)
        # adjust the value passed to waitKey according to needed fps
        if cv.waitKey(33) == ord('q'):
            break
    i += 1
cap.release()
cv.destroyAllWindows()