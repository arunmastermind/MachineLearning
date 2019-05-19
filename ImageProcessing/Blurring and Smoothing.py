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

    kernel = np.ones((15,15), np.float32)/255 #15*15=255
    smothed = cv2.filter2D(result, -1, kernel)

    blur = cv2.GaussianBlur(result, (15, 15), 0)
    median = cv2.medianBlur(result, 15)
    bilateral = cv2.bilateralFilter(result, 15, 75, 75)

    cv2.imshow('frame', frame)
    #cv2.imshow('mask', mask)
    cv2.imshow('result', result)
    cv2.imshow('smothed', smothed)
    cv2.imshow('blur', blur)
    cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()