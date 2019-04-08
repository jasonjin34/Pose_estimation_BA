import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

#Create a block image
#(512, 512 ,3) the shape of the image (row, columns,
img = np.zeros((512, 512, 3), np.uint8)
cv.line(img, (0, 0),(1024, 1024),(255, 0, 0), 5)

#drawing
cv.rectangle(img, (384, 0), (510, 128), (0, 250, 0), 3)
cv.circle(img, (447, 63), 63, (0, 0, 255), 1)

#adding text to images:
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (275, 275), font, 2, (255 , 255, 255), 2, cv.LINE_8)

plt.imshow(img)
plt.show()

img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("image with opencv", img)
cv.waitKey(0)
cv.destroyAllWindows()