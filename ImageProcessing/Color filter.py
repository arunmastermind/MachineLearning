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

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('result', result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()