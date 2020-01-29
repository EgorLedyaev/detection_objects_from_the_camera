import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
while (True):
    ret, frame = cap.read()
    cv.imshow("Frame",frame)
    print(frame)
    print(ret)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()