import cv2
import numpy as np

cap = cv2.VideoCapture(0)
#i was doing this for my olive green t-shirt
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_mask = np.array([80,80,30])
    upper_mask = np.array([130,120,70])

    mask = cv2.inRange(hsv, lower_mask, upper_mask)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #Morphology1
    kernel = np.ones((5,5), np.uint8)
    #erosion
    erosion = cv2.erode(mask, kernel, iterations=1)
    #diliation
    dilation = cv2.dilate(mask, kernel, iterations=1)

    # Morphology2
    #open
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    #close
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Morphology3 tophat and blackhat

    cv2.imshow('frame', frame)
    cv2.imshow('result', result)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()