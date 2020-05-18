from PIL import Image
import numpy as np
import cv2

img = cv2.imread("img6.bmp")
img_out = img.copy()

width, height, bit = np.shape(img)

for j in range(0,height) :
 for i in range(0,width) :
    if(img_out[i][j][0] >= 150):
      temp = 255
    else:
      temp = 0     
    img_out[i][j][0] = temp
    img_out[i][j][1] = temp
    img_out[i][j][2] = temp

cv2.imshow('image',img_out)
cv2.waitKey(0)
           
