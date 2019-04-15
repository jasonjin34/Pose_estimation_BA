import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from linedetection import cannyEdge

'''function use to divide the image into 6 sub images'''
def image_divider(image, row, coloum):
    '''save the divide image in the images list'''
    images = []
    image_row_size = int(len(image)/row)
    image_colum_size = int(len(image[0])/coloum)
    for index_row in range(row):
        for index_column in range(coloum):
            image_divide_temp = image[index_row*image_row_size:(index_row + 1)*image_row_size].copy()
            image_divide = []
            for index in range(len(image_divide_temp)):
                image_divide.append(image_divide_temp[index][index_column*image_colum_size:(index_column + 1)*image_colum_size ])
            images.append(image_divide)
    return images

def main():
    image = cv.imread('image/linedetect.png', 1)
    fig_divider = plt.figure(figsize=(18, 9))
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    images = image_divider(image, 2, 3)
    for index in range(6):
        fig_divider.add_subplot(231 + index)
        plt.imshow(images[index])
    plt.show()

if __name__ == '__main__':
    main()
