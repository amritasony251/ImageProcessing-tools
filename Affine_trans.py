from PIL import Image
import numpy as np
import cv2

img = cv2.imread("hist-equilised.png")
img_out1 = img.copy()
img_out2 = img.copy()
img_out3 = img.copy()
width, height, depth = np.shape(img)

'''print("1 : rotate left")
print("2 : rotate right")
print("3 : rotate 180 degree")

choice = int(input()) '''

'''for i in range(0,height):
   for j in range(0,width):
      img_out1[i][j] = img[j][i]

cv2.imshow("image",img_out1)
cv2.waitKey(0)  
cv2.destroyAllWindow()  

input('Press enter to continue')         

for i in range(0,height):
   for j in range(0,width):
      img_out2[i][j] = img[i][width-j]

cv2.imshow("image",img_out2)
cv2.waitKey(0)             

'''
for i in range(0,height):
   for j in range(0,width):
      img_out1[i][j] = img[height-1-i][j]

cv2.imshow("image",img_out1)
cv2.waitKey(0)            

