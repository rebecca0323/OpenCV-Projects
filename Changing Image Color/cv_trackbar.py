#Made by Rebecca Zhu 2/22/2020
#uses a track bar to determine the RBG values of a background

import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

#must toggle this to the right for the colors to show
switch = 'color/gray'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)

    #press escape key to exit
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()