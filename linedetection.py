import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

'''function use to divide the image into 6 sub images'''
def image_divider(image, row, coloum):
    '''save the divide image in the images list'''
    images = []
    image_row_size = int(len(image)/row)
    image_colum_size = int(len(image[0])/coloum)
    print(image_row_size, image_colum_size)
    for index_row in range(row):
        for index_column in range(coloum):
            image_divide_temp = image[index_row*image_row_size:(index_row + 1)*image_row_size].copy()
            image_divide = []
            for index in range(len(image_divide_temp)):
                image_divide.append(image_divide_temp[index][index_column*image_colum_size:(index_column + 1)*image_colum_size ])
            images.append(image_divide)
    return images

'''generate edge function '''
def cannyEdge(src,  min):
    src = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    dst = cv.Canny(src, min, min*2, apertureSize=3)
    #dst = cv.dilate(dst, None)
    return dst

image = cv.imread('image/sample_1.png', 1)
#cv.imshow('origin picture', image)
image_size = image.shape
x_size = image_size[0]
y_size = image_size[1]
ratio = x_size/y_size

'''lower resolutions'''
size = 1500
image = cv.resize(image, (size, int(size*ratio)))
#cv.imshow('origin image', image)
image_origin = image

image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
image = cannyEdge(image, 125)
cv.imshow('edge', image)

line_input_bool = 1

if line_input_bool == 1:
    Lines = cv.HoughLinesP(image, 1, np.pi/8, 30, minLineLength=30, maxLineGap=10)
elif line_input_bool == 2:
    Lines = cv.HoughLinesP(image, 1, np.pi/4, 10)

for line in Lines:
    x1, y1, x2, y2 = line[0]
    cv.line(image_origin,(x1, y1), (x2, y2), (0, 255, 0), 2)
cv.imshow('origin with line', image_origin)

image = cv.cvtColor(image_origin, cv.COLOR_BGR2RGB)
images = image_divider(image, 2, 3)

'''image plot'''
fig = plt.figure(figsize=(18, 9))
for index in range(6):
    fig.add_subplot(231 + index)
    plt.imshow(images[index])

plt.show()

cv.waitKey(0)
cv.destroyAllWindows()