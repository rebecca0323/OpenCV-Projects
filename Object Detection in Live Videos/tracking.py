#Made by Rebecca Zhu 2/22/2020

import cv2
import numpy as np

#call back function for creating trackbar
def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
#creates the trackbars
cv2.createTrackbar("Lower hue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower saturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Lower value", "Tracking", 0, 255, nothing)
cv2.createTrackbar("Upper hue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper saturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("Upper value", "Tracking", 255, 255, nothing)

while True:
    #video from camera
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("Lower hue", "Tracking")
    l_s = cv2.getTrackbarPos("Lower saturation", "Tracking")
    l_v = cv2.getTrackbarPos("Lower value", "Tracking")

    u_h = cv2.getTrackbarPos("Upper hue", "Tracking")
    u_s = cv2.getTrackbarPos("Upper saturation", "Tracking")
    u_v = cv2.getTrackbarPos("Upper value", "Tracking")

    #updates the mask and res based on the current trackbar positions
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

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