from PIL import Image, ImageDraw, ImageChops

image_1 = Image.open("4.jpg")
image_2 = Image.open("5.jpg")
img_1 = image_1
img_2 = image_2
img_1 = image_1.convert('L')
img_2 = image_2.convert('L')

diff = ImageChops.difference(img_1, img_2)
# показываем разницу
diff.show()
# выводим разницу
print(diff)
