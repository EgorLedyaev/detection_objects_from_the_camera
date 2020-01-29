from PIL import Image, ImageDraw, ImageChops
import cv2 as cv

cap_1 = cv.VideoCapture("4.jpg")
cap_2 = cv.VideoCapture("5.jpg")

ret_1, frame_1 = cap_1.read()
ret_2, frame_2 = cap_2.read()

#image_1 = Image.open("4.jpg")
#image_2 = Image.open("5.jpg")
image_1 = Image.open(frame_1)
image_2 = Image.open(frame_2)
#img_1 = image_1
#img_2 = image_2
img_1 = frame_1
img_2 = frame_2
#img_1 = image_1.convert('L')
#img_2 = image_2.convert('L')

diff = ImageChops.difference(img_1, img_2)
# показываем разницу
diff.show()
# выводим разницу
print(diff)
