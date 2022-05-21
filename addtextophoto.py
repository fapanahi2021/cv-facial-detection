#imported the opencv libray, وارد کردن کتابخانه مورد نظر
import cv2

#add an image, افزودن تصویر
image = 'test4.jpg'

#read the image, خواندن تصویر
img =  cv2.imread(image)

#show the image, نشان دادن تصویر
cv2.imshow("test4", img)

#add delay to closing the image, ایجاد وقفه
cv2.waitKey(0)

#resize the image, تغییر سایز تصویر
new_dimension = (100, 100)
img_resized = cv2.resize(img, new_dimension)

height, width, depth = img.shape
desired_height = 512
aspect_ratio = desired_height/width
dimension = (desired_height, height*aspect_ratio)
img_resized = cv2.resize(img, dimension)

#add text to image, اضافه کردن متن به تصویر
BLACK = (255,255,255)
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 1.1
font_color = BLACK
font_thickness = 2
text = 'Taghipanahi'
x,y = 10,650
img_text = cv2.putText(img_resized, text, (x,y), font, font_size, font_color, font_thickness, cv2.LINE_AA)

cv2.imwrite('test4_resized_text.jpg',img_text)

