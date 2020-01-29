from skimage.measure import compare_ssim
import imutils
import cv2 as cv
import time

cap = cv.VideoCapture(0)

ret, frame = cap.read()


#imageA = cv2.imread("6.jpg")
#imageB = cv2.imread("7.jpg")
imageB = frame

S =1

while S ==1:
    ret, frame = cap.read()
    imageA = frame
    grayA = cv.cvtColor(imageA, cv.COLOR_BGR2GRAY)
    grayB = cv.cvtColor(imageB, cv.COLOR_BGR2GRAY)

    grayA = cv.blur(grayA, (5, 5))
    #cv.imshow("BLur", grayA)
    grayB = cv.blur(grayB, (5, 5))
    #cv.imshow("BLur", grayB)

    grayA = cv.erode(grayA, (3, 3), iterations=2)
    #cv.imshow("Erode", grayA)

    grayA = cv.dilate(grayA, (3, 3), iterations=2)
    #cv.imshow("Dilate", grayA)

    grayB = cv.erode(grayB, (3, 3), iterations=2)
    #cv.imshow("Erode", grayB)

    grayB = cv.dilate(grayB, (3, 3), iterations=2)
    #cv.imshow("Dilate", grayB)

    (score, diff) = compare_ssim(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")
    print("SSIM: {}".format(score))

    thresh = cv.threshold(diff, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)[1]
    cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        (x, y, w, h) = cv.boundingRect(c)
        cv.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)

    imageB = imageA
    cv.imshow("Original", imageA)
    cv.imshow("Modified", imageB)
    #cv.imshow("Diff", diff)
    cv.imshow("Thresh", thresh)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()

