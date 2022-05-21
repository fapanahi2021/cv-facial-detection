#import the essential libraries, وارد کردن کتابخانه های مورد نیاز
import cv2
import matplotlib.pyplot as plt

#read the image, خواندن تصویر
image= cv2.imread('test.jpg')
original_image= image

#grey the image, خاکستری کردن تصویر
gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edges= cv2.Canny(gray, 50,200)


contours, hierarchy= cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)


sorted_contours= sorted(contours, key=cv2.contourArea, reverse= True)


#for circle,   برای لیبل گذاری حلقه for
for (i,c) in enumerate(sorted_contours):
    M= cv2.moments(c)
    cx= int(M['m10']/M['m01'])
    cy= int(M['m01']/M['m01'])
    cv2.putText(image, text= str(i+1), org=(cx,cy),
            fontFace= cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0,0,0),
            thickness=2, lineType=cv2.LINE_AA)

    
#show the image, نشان دادن تصویر
plt.imshow(image)
plt.show()
