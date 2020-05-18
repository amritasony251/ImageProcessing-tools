import numpy as np
import cv2
from PIL import Image

# X and F are numpy matrices
def convolve_np(X, F):
    X_height = X.shape[0]
    X_width = X.shape[1]
    print(X.shape[2])
    print(X[10][10])

    F_height = 3
    F_width = 3
    
    H = (F_height - 1) / 2
    W = (F_width - 1) / 2
    
    out = np.zeros((X_height, X_width))
    
    for i in np.arange(H, X_height-H):
        for j in np.arange(W, X_width-W):
            sum = 0
            for k in np.arange(-H, H+1):
                for l in np.arange(-W, W+1):
                    a = X[int(i+k)][int(j+l)][2]
                    w = F[int(H+k)][int(W+l)]
                    sum += (w*a)
            out[int(i)][int(j)] = sum
        
    return out

X = cv2.imread("img6.bmp")

F = np.array(
        [[-2, -1, 0],
        [-1, -1, 1],
        [0, 1, 2]])
        

res = convolve_np(X, F)

for i in np.arange(0, X.shape[0]):
    for j in np.arange(0, X.shape[1]):
      X[j][i][0] = res[j][i]
      X[j][i][1] = res[j][i]
      X[j][i][2] = res[j][i]
      

cv2.imwrite('images/convolve.jpg', X)

cv2.imshow('image',X)
cv2.waitKey(0)
cv2.destroyAllWindows()

