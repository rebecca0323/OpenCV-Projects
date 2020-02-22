import cv2
import numpy as np

# img = cv2.imread('lena.jpg', 1)
img = np.zeros([512,512,3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,0), 5)
img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 5)

img = cv2.rectangle(img, (300,0), (400,100), (0, 255, 0), 5)
img = cv2.circle(img, (400,200), 63, (0, 255, 0), -1)
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "Hi, test output", (10, 400), font, 4, (255,255,255), 10)

cv2.imshow('image', img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
