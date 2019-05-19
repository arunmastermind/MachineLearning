import cv2
import numpy as np

img = cv2.imread('taj.jpeg')

img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,215, 255, cv2.THRESH_BINARY)

mask_inv = cv2.bitwise_not(mask)

img_fg = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img_fg', img_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()