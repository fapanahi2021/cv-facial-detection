import numpy as np
import cv2

img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
img= cv2.resize(img, (400,400))
#resize

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

