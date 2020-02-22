# written by Rebecca Zhu 2/22/2020
# detects blue objects in live videos

import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #hsv values for blue
    l_b = np.array([110, 50, 50])
    u_b = np.array([130,255,255])

    mask = cv2.inRange(hsv, l_b, u_b)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    #escape key to quit
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()