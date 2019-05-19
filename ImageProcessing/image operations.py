import cv2
import numpy as np

img = cv2.imread('taj.jpeg', cv2.IMREAD_COLOR)

img[55,55]= [255,255,255]
px =img[55,55]

#print(px)

#roi=img[100:150, 100:150]
#print(roi)

img[100:150, 100:150] = [255,255,255]
tajface = img[66:190, 6:131]

cv2.imshow('IMAGE', img)
cv2.imshow('IMAGE2', tajface)
cv2.waitKey(0)
cv2.destroyAllWindows()
