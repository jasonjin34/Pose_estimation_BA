import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

#load an color image
file_path_lena = 'Image/lena.png'
image_color = cv.imread(file_path_lena, 1)
image_grayscale = cv.cvtColor(image_color, cv.COLOR_RGB2GRAY)

#normal color
cv.imshow('image with color', image_color)
#grayscale
cv.imshow('grayscale image', image_grayscale)
cv.waitKey(0)
cv.destroyAllWindows()

#using matplot for displaying image
plt.imshow(image_grayscale, cmap='gray', interpolation='bicubic')
plt.show()