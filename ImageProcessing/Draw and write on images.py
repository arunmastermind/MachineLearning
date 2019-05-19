import cv2
import numpy as np

img = cv2.imread('taj.jpeg', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15)
cv2.rectangle(img, (15,25), (200,150), (0,255,0), 15)
cv2.circle(img, (100,63), 55, (0,0,255), -1)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
cv2.polylines(img, [pts], True, (0,255,255), 5)

font = cv2.FONT_ITALIC
cv2.putText(img, 'Arun Kumar', (0,131), font, 1, (0,255,0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
