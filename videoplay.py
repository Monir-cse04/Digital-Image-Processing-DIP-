import cv2
import numpy as np
import time

cap = cv2.VideoCapture("Monir.avi")
while(True):
    ret, frame = cap.read()
    time.sleep(1/20) #inverse of frame rate , and it stays in screen 1/20 sec

    cv2.imshow('webcam', frame)

    #color to gray webCam
    # img_gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('webcam', img_gray)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
cv2.destroyAllWindows()

#it just captures a photo from webcam
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# ret, frame = cap.read()
#
# if ret:
#     cv2.imshow("Camera", frame)
#
# cv2.waitKey(0)
# cap.release()
# cv2.destroyAllWindows()

