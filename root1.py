from skimage.measure import compare_ssim
import cv2
import numpy as np
import cv2 as cv
import time

cap = cv.VideoCapture(0)

first_ret, first_frame = cap.read()

before = first_frame

s = 1
while s == 1:
    ret, frame = cap.read()
    after = frame
    before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
    after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)

    before_gray = cv.blur(before_gray, (5, 5))
    # cv.imshow("BLur", before_gray)
    after_gray = cv.blur(after_gray, (5, 5))
    # cv.imshow("BLur", after_gray)

    before_gray = cv.erode(before_gray, (3, 3), iterations=2)
    # cv.imshow("Erode", before_gray)

    gbefore_gray = cv.dilate(before_gray, (3, 3), iterations=2)
    # cv.imshow("Dilate", grayA)

    after_gray = cv.erode(after_gray, (3, 3), iterations=2)
    # cv.imshow("Erode", after_gray)

    after_gray = cv.dilate(after_gray, (3, 3), iterations=2)
    # cv.imshow("Dilate", after_gray)

    # считаем ssim (степень схожести)
    (score, diff) = compare_ssim(before_gray, after_gray, full=True)
    print("Image similarity", score)
    #print(diff)

    # преобразование в 8-бит
    diff = (diff * 255).astype("uint8")

    # получаем области
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    mask = np.zeros(before.shape, dtype='uint8')
    filled_after = after.copy()

    for c in contours:
        area = cv2.contourArea(c)
        if area > 40:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 2)
            cv2.drawContours(mask, [c], 0, (0, 255, 0), -1)
            cv2.drawContours(filled_after, [c], 0, (0, 255, 0), -1)

    before = after
    cv2.imshow('before', before)
    cv2.imshow('after', after)
    cv2.imshow('diff', diff)
    cv2.imshow('mask', mask)
    cv2.imshow('filled after', filled_after)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()