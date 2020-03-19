import math
import cv2
import numpy as np
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path,dtype=np.uint8),-1)
    return cv_img

img = cv_imread('GrayImages/GaussScale/gray高斯多尺度平滑1.jpg')
cv2.startWindowThread()
