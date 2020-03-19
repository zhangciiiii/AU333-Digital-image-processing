import math
import cv2

img = cv2.imread('GrayImages/fortest.jpg')
cv2.startWindowThread()
cv2.imshow('pirate',img)
cv2.waitKey(0)

cv2.destroyAllWindows()