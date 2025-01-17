import cv2
import numpy as np

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #print(x, ", ", y)
        #font = cv2.FONT_HERSHEY_COMPLEX
        #strXY = str(x) + ", " + str(y)
        #cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)

        cv2.imshow('image', img)

#img = cv2.imread('lena_name.jpg')
img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()