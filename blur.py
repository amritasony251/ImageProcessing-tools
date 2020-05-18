import cv2
import numpy as np
from PIL import Image

img = cv2.imread("img5.jpg")
height, width, depth = np.shape(img)

kernel = [[2.0/9.0, 1.0/9.0, 1.0/9.0],
          [1.0/9.0, 1.0/9.0, 1.0/9.0],
          [1.0/9.0, 1.0/9.0, 5.0/9.0]]
H = int(len(kernel)/2)

for i in range(H, height-H-1):
    for j in range(H, width-H-1):
        sum = 0.0
        for k in range(-H, H+1):
           for l in range(-H, H+1):
               sum = sum + kernel[k+H][l+H]*img[i+k][j+l]
        img[i][j] = sum
        #img[i][j][1] = sum
        #img[i][j][2] = sum

cv2.imshow('image',img)
cv2.waitKey(0)               
