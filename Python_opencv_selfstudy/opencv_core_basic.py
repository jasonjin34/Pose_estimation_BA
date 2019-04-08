import cv2 as cv
import numpy as np

img = cv.imread('Image/lena.png')
cv.imshow('test', img)
#split the b,g,r planes
b, g, r = cv.split(img)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)

#check the pixel value by its row and column coordinates
#check the imagg type
height, width, channels = img.shape
print('the width of the image: %s and the height of the image is %s' %(str(height),str(width)))
print('the type of image is: ' + str(type(img)))

px_test = img[100,200]
print(px_test)
print(img.dtype)

cv.waitKey(0)
cv.destroyAllWindows()